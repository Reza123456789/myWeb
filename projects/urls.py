from django.urls import path
from . import views

urlpatterns = [
    path('',views.projects , name='Projects'),
    path('project/<str:pk>/',views.Project,name="project"),
    path('create-project/',views.createProject,name='createProject'),
    path('updateProject/<str:pk>/',views.updateProject,name='updateProject'),
    path('deleteProject/<str:pk>/',views.deleteProject,name='deleteProject'),


]