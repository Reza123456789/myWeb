from django.db import models
from django.contrib.auth.models import User
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
    class Meta:
        ordering=['-Vote_ratio','-Vote_total','title']
    
    
    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset

    @property
    def getVoteCount(self):
        reviews=self.review_set.all() 
        upVote=reviews.filter(value='up').count()
        totalVote=reviews.count()
        try:
            ratio=(upVote/totalVote)*100
            self.Vote_total=totalVote
            self.Vote_ratio=ratio
            self.save()
        except ZeroDivisionError:
            self.Vote_total=totalVote
            self.Vote_ratio=ratio
            self.save()
            


class review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    owner = models.ForeignKey(profile, null=True , on_delete=models.SET_NULL)
    project = models.ForeignKey(project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    class Meta:
         unique_together=[['owner' , 'project']]
         
    def __str__(self):
        return self.value




class Tag(models.Model):
    name=models.CharField(max_length=200)
    id=models.UUIDField(default=uuid.uuid4,unique=True
                        ,primary_key=True,editable=False)
    def __str__(self):
        return self.name