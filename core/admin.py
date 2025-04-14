from django.contrib import admin
from .models import Profile, Post, LikePost, FollowerCount
# Register your models here.

admin.site.register(Profile) # shows models classes in admin
admin.site.register(Post)
admin.site.register(LikePost) 
admin.site.register(FollowerCount) 