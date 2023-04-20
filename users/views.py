from django.shortcuts import render , redirect
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from .models import profile
# Create your views here.

def loginUser(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=User.objects.get(username=username)
            print(username)
            print(user)
            print(User.objects.all())
        except:
            messages.error(request , 'Username does not Exist')
        
        user=authenticate(request,username=username,password=password) 

        if user is not None:
            login(request , user)
            return redirect('profiles')
        else:
            messages.error(request , 'Username Or pass are incorrect')
        
    return render(request,'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.success(request, 'User was successfully Logged Out')
    return redirect('login')

def profiles(request):
    profiles=profile.objects.all()
    context={'profiles':profiles}
    return render(request,'users/profiles.html',context)

def userProfiles(request,pk):
    profiles=profile.objects.get(id=pk)
    topSkills = profiles.skill_set.exclude(description__exact="")
    otherSkills = profiles.skill_set.filter(description="")
    context={'profile':profiles , 'topSkills': topSkills,
               "otherSkills": otherSkills}
    return render(request, 'users/user-Profile.html',context)
