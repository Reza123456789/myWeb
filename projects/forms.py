from django.forms import ModelForm
from django import forms
from .models import project , review
class ProjectForm(ModelForm):
    class Meta:
        model=project
        fields=['title','feuchered_image','descriptions','demo_link','source_link','tags']
        widgets={
            'tags':forms.CheckboxSelectMultiple(),
        }
    def __init__(self,*args,**kwargs):
        super(ProjectForm,self).__init__(*args, **kwargs)

        for name ,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class reviewForm(ModelForm):
    class Meta:
        model=review
        fields = ['value', 'body']
        labels = {'value':'Place your vote','body':'Add a comment with your vote'}

    def __init__(self, *args, **kwargs):
        super(reviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
