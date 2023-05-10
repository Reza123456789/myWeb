from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save , post_delete
import uuid
# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    first_name=models.CharField(max_length=200,blank=True,null=True)
    last_name=models.CharField(max_length=200,blank=True,null=True)
    short_bio=models.CharField(max_length=200,blank=True,null=True)
    username=models.CharField(max_length=200,blank=True,null=True)
    location=models.CharField(max_length=200,blank=True,null=True)
    bio=models.TextField(blank=True,null=True)
    profile_img=models.ImageField(null=True,upload_to='images/profiles',blank=True,default='profiles/user-default.png')
    age=models.IntegerField(default=0,null=True,blank=True)
    email=models.EmailField(max_length=500,null=True,blank=True)
    social_website=models.CharField(max_length=200,blank=True,null=True)
    social_youtube=models.CharField(max_length=200,blank=True,null=True)
    social_linkedin=models.CharField(max_length=200,blank=True,null=True) 
    social_twitter=models.CharField(max_length=200,blank=True,null=True) 
    social_github=models.CharField(max_length=200,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True
                        ,primary_key=True,editable=False)
    def __str__(self):
        return str(self.user.username)
    class Meta:
        ordering=['created']

class Skill(models.Model):
    owner=models.ForeignKey(profile,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,blank=True,null=True)
    description=models.TextField(null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True
                        ,primary_key=True,editable=False)
    def __str__(self):
        return str(self.name)
    
class Message(models.Model):
    sender=models.ForeignKey(profile,null=True,blank=True,on_delete=models.SET_NULL)
    recipient=models.ForeignKey(profile,null=True,on_delete=models.CASCADE,related_name='payams')
    subject=models.CharField(max_length=200,blank=True,null=True)
    sender_name=models.CharField(max_length=200,blank=False,null=True)
    body=models.TextField()
    created=models.DateTimeField(auto_now=True,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    is_read=models.BooleanField(default=False,null=True,blank=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True
                        ,primary_key=True,editable=False)
    def __str__(self):
        return str(self.subject)
    
    class Meta:
        ordering=['is_read','-created']




