from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def index(request):
    return render(request,'awaremeapp/index.html')

@login_required(login_url='login')
def orgDetails(request):
    Instance1=OrgModel.objects.all()
    return render(request,'awaremeapp/info.html',{'model':Instance1})

def orgRegister(request):
    if request.user.is_authenticated:
        return redirect('details')
    else:
        form1=OrgUser()
        form=Organisation()
        if request.method =='POST':
            form1=OrgUser(request.POST)
            form=Organisation(request.POST)
            if form1.is_valid() and form.is_valid():
                form1.save()
                form.save()
                user = form1.cleaned_data.get('username')
                messages.success(request,'account created successfully'+ user)
                return redirect('login')
            else:
                print("error!")
        else:
            form1=OrgUser()
            form=Organisation()
        return render(request,'awaremeapp/registration.html',{'form1':form1,'form':form})

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('index')

def user_login(request):
    if request.user.is_authenticated:
        return redirect('details')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                    login(request,user)
                    return orgDetails(request)      
            else:
                messages.info(request,'username or password incorrect')
        return render(request,'awaremeapp/login.html')
        
        











