from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.loginUser , name='login'),
    path('logout/',views.logoutUser , name='logout'),
    path('register/', views.registerUser , name='register'),
    path('',views.profiles,name='profiles'),
    path('profile/<str:pk>/',views.userProfiles,name='user-profiles'),
    path('account/',views.userAccount,name='account'),
    path('edit-acoount/',views.editAccount , name='editAcc'),

    path('create-skill/',views.createSkill ,name='create-skill'),
    path('update-skill/<str:pk>/',views.updateSkill ,name='update-skill'),
    path('delete-skill/<str:pk>/',views.deleteSkill ,name='delete-skill'),


    path('inbox/',views.inbox ,name='inbox'),
    path('message/<str:pk>/',views.message ,name='message'),
    path('send-message/<str:pk>/',views.createMessage,name='send-message')



]