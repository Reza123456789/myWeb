from django.forms import ModelForm
from django import forms
from .models import profile
class ProjectForm(ModelForm):
    class Meta:
        model=profile
        fields=['first_name','last_name','username','bio','profile_img','age','email']
        
        