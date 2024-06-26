from django.forms import ModelForm, widgets
from django import forms
from .models import Project, Review

class projectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['vote_ratio', 'vote_total', 'owner']

        widgets ={
            'tags':forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(projectForm,self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

        # self.fields['title'].widget.attrs.update({'class':'input', 'placeholder':'Add title'})
        # self.fields['description'].widget.attrs.update({'class':'input', 'placeholder':'Add title'})

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote'
        }
    
    def __init__(self, *args, **kwargs):
        super(ReviewForm,self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})