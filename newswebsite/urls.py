from django.conf.urls import url, include
from django.contrib import admin
from . import views
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    url(r'^$', views.home,name='home'),
    url(r'^page1/$', views.page1, name='page1'),
    url(r'^page2/$', views.page2, name='page2'),
    url(r'^politics/$', views.politics, name='politics'),
    url(r'^world/$', views.world, name='world'),
    url(r'^business/$', views.business, name='business'),
    url(r'^sport/$', views.sport, name='sport'),
    url(r'^editor/$', views.editor, name='editor'),
    url(r'^register/', views.register, name='register'),
    url(r'^comments/',views.CommentList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

