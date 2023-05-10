from django.shortcuts import render , redirect
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import customUserCreationForm , ProfileForm ,SkillForm , messageForm
from django.contrib import messages
from .util import searchProfile , paginatePages

from django.http import HttpResponse
from .models import profile , Skill , Message
# Create your views here.

def loginUser(request):
    page='login'
    context={'page':page}
    
    if request.method == 'POST':
        username=request.POST['username'].lower()
        password=request.POST['password']
        try:
            user=User.objects.get(username='username')
            print(username)
            print(user)
            print(User.objects.all())
        except:
            messages.error(request , 'Username does not Exist')
        
        user=authenticate(request,username=username,password=password) 

        if user is not None:
            login(request , user)
            messages.info(request,'User Logged in sucssessfully')
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')
        else:
            messages.error(request , 'Username Or pass are incorrect')
        
    return render(request,'users/login_register.html',context)


def logoutUser(request):
    logout(request)
    messages.success(request, 'User was successfully Logged Out')
    return redirect('login')

def registerUser(request):
    form=customUserCreationForm()
    page='register'

    if request.method =='POST':
        form=customUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()

            messages.info(request , 'User Created Sucssesfully')
            login(request , user)
            return redirect('editAcc')
        
        else:
            messages.error(request,'An error occurd during registration')

    context={'page':page , 'form':form}
    return render(request,'users/login_register.html' , context)



def profiles(request):
    profile , search_query=searchProfile(request)

    custom_range,profile=paginatePages(request,profile,4)
    context={'profiles':profile, 'search_query':search_query,'custom_range':custom_range,}
    return render(request,'users/profiles.html',context)

def userProfiles(request,pk):
    profiles=profile.objects.get(id=pk)
    topSkills = profiles.skill_set.exclude(description__exact="")
    otherSkills = profiles.skill_set.filter(description="")
    context={'profile':profiles , 'topSkills': topSkills,
               "otherSkills": otherSkills}
    return render(request, 'users/user-Profile.html',context)
@login_required(login_url='login')
def userAccount(request):
    profile=request.user.profile
    skills = profile.skill_set.all()
    context={'profile':profile , 'skills':skills}
    return render(request , 'users/account.html',context)

@login_required(login_url='login')
def editAccount(request):
    profile=request.user.profile
    form=ProfileForm(instance=profile)

    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')

    context={'form':form}
    return render(request , 'users/edit-profile.html',context)


def createSkill(request):
    profile=request.user.profile
    form=SkillForm()
    if request.method=='POST':
        form=SkillForm(request.POST)
        if form.is_valid():
            skill=form.save(commit=False)
            skill.owner=profile
            skill.save()
            return redirect('account')
    context={'form':form} 
    return render(request, 'users/skill_form.html',context)


def updateSkill(request , pk):
    profile=request.user.profile
    skill=profile.skill_set.get(id=pk)
    form=SkillForm(instance=skill)
    if request.method=='POST':
        form=SkillForm(request.POST , instance=skill)
        if form.is_valid():
            form.save()
            return redirect('account')
    context={'form':form} 
    return render(request, 'users/skill_form.html',context)

def deleteSkill(request , pk):
    profile=request.user.profile
    skill=profile.skill_set.get(id=pk)
    if request.method=='POST':
        skill.delete()
        return redirect('account')
    context={'object':skill}
    return render(request, 'delete_template.html',context)

def inbox(request):
    profile = request.user.profile
    payams=profile.payams.all()
    reade=profile.payams.filter(is_read=False).count()
    context={'payams':payams,'reade':reade}

    return render(request,'users/inbox.html',context)

def message(request,pk):
    profile = request.user.profile
    payam=profile.payams.get(id=pk)
    if payam.is_read==False:
        payam.is_read=True
        payam.save()
    context={'payams':payam}
    return render(request,'users/messages.html',context)

def createMessage(request,pk):
    recipient=profile.objects.get(id=pk)
    form=messageForm()
    try:
        sender=request.user.profile
    except:
        sender=None
    if request.method=='POST':
        form=messageForm(request.POST)
        if form.is_valid():
            x=form.save(commit=False)
            x.sender=sender
            x.recipient=recipient
            if request.user.profile:
                x.email=request.user.profile.email
                x.sender_name=request.user.profile.first_name
            x.save()
            return redirect('user-profiles', pk=recipient.id)
    context={'form':form}
    return render(request,'users/messageForm.html',context)

