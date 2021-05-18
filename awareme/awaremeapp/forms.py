from django import forms
from django.forms import ModelForm,TextInput,EmailInput,PasswordInput,Textarea
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 



class mission_register(ModelForm):
    class Meta:
        model = OrgDetail
        fields = ['user','Contact','mission','portfolio']
        widgets={
            'mission':Textarea(attrs={
                'class':"form-control",
                'style':'max-width:500px;max-height:200px',
                'placeholder':'organisation motive ...'
            }),
            'Contact':TextInput(attrs={
                'class':"form-control",
                'style':'max-width:500px;',
                # 'placeholder':'contact'
            }),
            'portfolio':TextInput(attrs={
                'class':"form-control",
                'style':'max-width:500px;',
                'placeholder':'https://example.com'
            }),
        }
class Donati(ModelForm):
    class Meta:
        model=Donation
        fields='__all__'
        widgets={
             'name':TextInput(attrs={
                'class':"form-control",
                'style':'max-width:500px;font-weight:bold;',
                'placeholder':'enter your name here'
            }),
             'email':EmailInput(attrs={
                'class':"form-control",
                'style':'max-width:500px;font-weight:bold;',
                'placeholder':'@'
            }),
             'amount':TextInput(attrs={
                'class':"form-control",
                'style':'max-width:500px;font-weight:bold;',
                'placeholder':'in rupees'
            }),
             'cardnumber':TextInput(attrs={
                'class':"form-control",
                'style':'max-width:500px;font-weight:bold;',
                'placeholder':''
            }),
        }

class Organisation(ModelForm):
    class Meta:
        model = OrgDetail
        fields = '__all__'
        exclude=['user']
        widgets={
            'mission':Textarea(attrs={
                'class':"form-control",
                'style':'max-width:500px;max-height:200px',
                'placeholder':'mission'
            }),
            'Contact':TextInput(attrs={
                'class':"form-control",
                'style':'max-width:300px;',
                'placeholder':'contact'
            }),
            'portfolio':TextInput(attrs={
                'class':"form-control",
                'style':'max-width:300px;',
                'placeholder':'http://example.com'
            }),
        }

class Formfeed(ModelForm):
    class Meta:
        model=OrgFeed
        fields='__all__'
        exclude=['user']


        widgets={
            'title':TextInput(attrs={
                'class':"form-control",
                'style':'width:80vw;max-height:200px',
                # 'placeholder':'Title'
            }),
            'author':TextInput(attrs={
                'class':"form-control",
                'style':'width:80vw;',
                # 'placeholder':'Author name'
            }),
            'locations':TextInput(attrs={
                'class':"form-control",
                'style':'width:80vw;',
                # 'placeholder':'enter location'
            }),
            'brief':Textarea(attrs={
                'class':"form-control",
                'style':'width:80vw;',
                'placeholder':'article..'
            }),
        }


