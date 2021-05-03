from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class OrgUser(UserCreationForm):
    class Meta:
        model = User
        fields=['username','first_name','email','password1','password2']
        



class mission_register(ModelForm):
    class Meta:
        model = OrgDetail
        fields = '__all__'

class Organisation(ModelForm):
    class Meta:
        model = OrgDetail
        fields = '__all__'
        exclude=['user']

class Formfeed(ModelForm):
    class Meta:
        model=OrgFeed
        fields='__all__'


