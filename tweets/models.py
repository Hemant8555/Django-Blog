from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class post(models.Model):
    author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000, blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    image = models.ImageField(upload_to="media/images/", blank=True, null=True)

    def __str__(self):
        return self.content[:10]


class comment(models.Model):
    content = models.TextField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_connected = models.ForeignKey(post, on_delete=models.CASCADE)
