from django.db import models
from django.contrib.auth import get_user_model
import uuid # for generating unique id for each Post 
from datetime import datetime
# Create your models here.
User= get_user_model() # model of currently loaded user 

class Profile(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    id_user= models.IntegerField()
    bio= models.TextField(blank=True, )
    profileimg= models.ImageField(upload_to='profile_images', default='14.jpg')
    location= models.CharField(max_length=225, blank=True)

    def __str__(self):
        return self.user.username # this will show usernames of user in admin pannel, we can skip this 
    

class Post(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4)
    user= models.CharField(max_length=225)
    image= models.ImageField(upload_to='post_images')
    caption= models.TextField()
    created_at= models.DateTimeField(default=datetime.now)
    no_of_likes= models.IntegerField(default=0)

    def __str__(self):
        return self.user
    

class LikePost(models.Model):
    post_id= models.CharField(max_length=255)
    username= models.CharField(max_length=225)

    def __str__(self):
        return self.username
    

class FollowerCount(models.Model):
    follower= models.CharField(max_length=255)
    user= models.CharField(max_length=225)

    def __str__(self):
        return self.user