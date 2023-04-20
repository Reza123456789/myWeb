from django.db import models
from users.models import profile
import uuid

class project(models.Model):
    owner=models.ForeignKey(profile,null=True,blank=True,on_delete=models.SET_NULL)
    title=models.CharField(max_length=200)
    descriptions=models.TextField(blank=True,null=True)
    demo_link=models.CharField(max_length=2000,null=True,blank=True)
    source_link=models.CharField(max_length=2000,null=True,blank=True)
    feuchered_image=models.ImageField(null=True,blank=True,default='default.jpg')
    tags=models.ManyToManyField('Tag', blank=True)
    Vote_total=models.IntegerField(default=0,null=True,blank=True)
    Vote_ratio=models.IntegerField(default=0,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True
                        ,primary_key=True,editable=False)
    def __str__(self):
        return self.title
class review(models.Model):
    VOTE_TYPE = (
        ('up','Up Vote'),
        ('down','Down Vote')
    )
    project=models.ForeignKey(project,on_delete=models.CASCADE)
    value=models.CharField(max_length=200,choices=VOTE_TYPE)
    body=models.TextField(null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True
                        ,primary_key=True,editable=False)
    def __str__(self):
        return self.value
class Tag(models.Model):
    name=models.CharField(max_length=200)
    id=models.UUIDField(default=uuid.uuid4,unique=True
                        ,primary_key=True,editable=False)
    def __str__(self):
        return self.name