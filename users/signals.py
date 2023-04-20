from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save , post_delete
from.models import profile

def createProfile(sender,instance,created,**kwargs):
    if created:
        user=instance
        Profile=profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            first_name=user.first_name ,
        )

def deleteUser(sender,instance,**kwargs):
    user=instance.user
    user.delete()

    
post_save.connect(createProfile,sender=User)
post_delete.connect(deleteUser,sender=profile)

    
    