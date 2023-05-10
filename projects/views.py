from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .util import searchProjects , paginatePages
from django.contrib.auth.models import User
from .models import project, review
from django.contrib import messages
from .forms import ProjectForm , reviewForm

def projects(request):
    projects,search_query=searchProjects(request)
    
    custom_range , projects =paginatePages(request,projects,6)

    content={'projects':projects,'search_query':search_query,'custom_range':custom_range}
    return render(request, 'projects/projects.html',content)

def Project(request,pk):
     projectObj=project.objects.get(id=pk)
     form=reviewForm()
     if request.method == 'POST':
        try:
            form=reviewForm(request.POST)
            review = form.save(commit=False)
            review.project = projectObj
            review.owner = request.user.profile
            review.save()
            projectObj.getVoteCount
            return redirect('project', pk=projectObj.id)
            

        except:
            form=reviewForm()
            messages.error(request, 'Your submit a review before!')
            return redirect('project', pk=projectObj.id)
     print(projectObj.__dict__)
     print(dir(projectObj))


     return render(request,'projects/single-projects.html', {'project': projectObj, 'form': form})


@login_required(login_url="login")
def createProject(request):
    profile=request.user.profile
    form=ProjectForm()
    
    if request.method =='POST':
        
        form=ProjectForm(request.POST , request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.owner=profile
            project.save()
            return redirect('account')

    context={'form':form}
    return render(request , "projects/project-form.html",context) 

@login_required(login_url="login")
def updateProject(request,pk):
    profile=request.user.profile
    project1 = profile.project_set.get(id=pk)
    form=ProjectForm(instance=project1)
    if request.method =='POST':
        form=ProjectForm(request.POST,request.FILES,instance=project1)
        if form.is_valid():
            form.save()
            return redirect('Projects')

    context={'form':form}
    return render(request , "projects/project-form.html",context) 

@login_required(login_url="login")
def deleteProject(request,pk):
    profile=request.user.profile
    ptiwd=profile.project_set.get(id=pk)
    context={'object':ptiwd}
    if request.method=='POST':
        ptiwd.delete()
        return redirect('account')
    return render(request,'delete_template.html',context)
    
