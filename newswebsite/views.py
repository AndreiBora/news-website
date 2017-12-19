from django.shortcuts import render
from .models import Comment
from .form import CommentForm, UserRegistrationForm,CommentForm2
from django.utils import  timezone
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import urllib.request
import json
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CommentSerializer



def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather'
    query = 'Eindhoven'
    key = '483b697a7c6cf81c6f5f63fd53d98abb'

    u = urllib.request.urlopen(url + '?q=' + query + '&APPID=' + key)
    data = u.read().decode('utf8')
    weather = json.loads(data)
    temperature = format((float(weather['main']['temp']) - 273.15),'.1f')
    humidity = weather['main']['humidity']
    description = weather['weather'][0]['description']

    return render(request, 'newswebsite/index.html',
                  {'temperature': temperature, 'humidity': humidity, 'description': description})


@login_required
def page1(request):
    comments = Comment.objects.all().filter(page=1).order_by('time');
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.time = timezone.now()
            comment.page = 1
            comment.user = User.objects.get(username=request.user.username)
            comment.save()

            return render(request, 'newswebsite/page1.html', {'comments': comments, 'form': form})
    else:
        form = CommentForm()
    return render(request,'newswebsite/page1.html',{'comments':comments,'form':form})

@login_required
def page2(request):
    comments = Comment.objects.all().filter(page=2).order_by('time');
    if request.method == "POST":
        form = CommentForm2(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.time = timezone.now()
            comment.page = 2
            comment.user = User.objects.get(username=request.user.username)

            comment.save()

            return render(request, 'newswebsite/page2.html', {'comments': comments, 'form': form})
    else:
        form = CommentForm2()
    return render(request, 'newswebsite/page2.html', {'comments': comments, 'form': form})



def politics(request):
    return render(request,'newswebsite/politics.html')

def world(request):
    return render(request,'newswebsite/world.html')

def business(request):
    return render(request,'newswebsite/business.html')

def sport(request):
    return render(request,'newswebsite/sport.html')

def editor(request):
    return render(request,'newswebsite/editor.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'newswebsite/register.html', {'form' : form})

# url comments/

class CommentList(APIView):
    def get(self,request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data)

    def post(self,request):
        pass