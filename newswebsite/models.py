from django.db import models
from django.utils import timezone

# Create your models here.


class Comment(models.Model):
    user = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    text = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    page = models.IntegerField()

    def submit(self):
        self.time = timezone.now()
        self.save()
        self.full_clean()

    def __str__(self):
        return self.text

