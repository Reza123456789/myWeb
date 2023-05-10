from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import profile , Skill , Message
class customUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','email','username','password1','password2']
        labels={'first_name':'Name','email':'Email','username':'Username','password1':'Password','password2':'Confirm Password'}
        
    def __init__(self,*args,**kwargs):
        super(customUserCreationForm,self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
            
class ProfileForm(ModelForm):
    class Meta:
        model=profile
        fields=['first_name','last_name','username','profile_img','email','short_bio','bio','location','age','social_website','social_youtube','social_linkedin','social_twitter','social_github']

    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        
class SkillForm(ModelForm):
    class Meta:
        model=Skill
        fields='__all__'
        exclude=['owner']
    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class messageForm(ModelForm):
    class Meta:
        model=Message
        fields=['subject','sender_name','body','email']
        labels={
            'subject':'subject',
            'sender_name':'Your Name',
            'body':'your Message',
            'email':'Your Email',

        }
    def __init__(self, *args, **kwargs):
        super(messageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
