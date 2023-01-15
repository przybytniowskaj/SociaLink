from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
from django import templatetags

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to='profile_photos', default='default_photo.png')
    location = models.CharField(blank = True, max_length=100)
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4 ,max_length=500)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to="post_images", blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user


class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Followers(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user

class Comment(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.username
