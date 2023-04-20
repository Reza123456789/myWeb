from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import project
from .forms import ProjectForm

def projects(request):
    projects=project.objects.all()
    content={'projects':projects}
    return render(request, 'projects/projects.html',content)

def Project(request,pk):
     projectObj=project.objects.get(id=pk)
    
     return render(request,'projects/single-projects.html',{'project':projectObj})

@login_required(login_url="login")
def createProject(request):
    form=ProjectForm()
    
    if request.method =='POST':
        form=ProjectForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Projects')

    context={'form':form}
    return render(request , "projects/project-form.html",context) 

@login_required(login_url="login")
def updateProject(request,pk):
    project1 = project.objects.get(id=pk)
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
    ptiwd=project.objects.get(id=pk)
    context={'object':ptiwd}
    if request.method=='POST':
        ptiwd.delete()
        return redirect('Projects')
    return render(request,'projects.delete_template.html',context)
    
