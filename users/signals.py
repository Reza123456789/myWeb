from django.contrib.auth.models import User
from django.shortcuts import render , redirect
from django.dispatch import receiver
from django.db.models.signals import post_save , post_delete
from.models import profile 
from django.conf import settings
from django.core.mail import send_mail

def createProfile(sender,instance,created,**kwargs):
    if created:
        user=instance
        Profile=profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            first_name=user.first_name ,
        )
        send_mail(
            "OOOh BaBy Welcome to My website",
            "Have Fun And Enjoy the Best Website Around The world,But Just Don't Be toxic and dont abuse my Developers",
            settings.EMAIL_HOST_USER,
            [Profile.email],
            fail_silently=False,
        )

def updateUser(sender,instance,created,**kwargs):
    profile=instance
    user=profile.user
    if created==False:
        user.first_name=profile.first_name
        user.username=profile.username
        if profile.email:
            user.email=profile.email
        print(instance,instance.username,instance.email)
        user.save()


def deleteUser(sender,instance,**kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass

    
post_save.connect(createProfile,sender=User)
post_save.connect(updateUser,sender=profile)
post_delete.connect(deleteUser,sender=profile)


    
    