from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# @login_required(login_url='login')
def index(request):
    return render(request,'awaremeapp/index.html')

    
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
                messages.success(request,'account created successfully' + user)
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
                    return redirect('listFeed')      
            else:
                messages.info(request,'username or password incorrect')
        return render(request,'awaremeapp/login.html')




def orgList(request):
    Instance1=OrgDetail.objects.all()
    return render(request,'awaremeapp/info.html',{'model':Instance1})

@login_required(login_url='login')
def org_profile(request,pk_value):
    orgPk=OrgDetail.objects.get(id=pk_value)
    orgInfo=OrgDetail.objects.all()
    context={'orgInfo':orgInfo,'orgPk':orgPk}
    return render(request,'awaremeapp/org_profile.html',context)

@login_required(login_url='login')
def createFeed(request):
    form=Formfeed()
    if request.method=='POST':
        form=Formfeed(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listFeed')
    context={'form':form}
    return render(request,'awaremeapp/feed_form.html',context)


def listFeed(request):
    feed=OrgFeed.objects.all()
    context={'feed':feed}
    return render(request,'awaremeapp/list_feed.html',context)



def newsFeed(request,pk):
    news=OrgFeed.objects.all()
    newspk=OrgFeed.objects.get(id=pk)
    context={'news':news,'newspk':newspk}
    return render(request,'awaremeapp/news_feed.html',context)

@login_required(login_url='login')
def updateFeed(request,pk):
    upnewspk=OrgFeed.objects.get(id=pk)
    form=Formfeed(instance=upnewspk)
    if request.method=='POST':
        form=Formfeed(request.POST,instance=upnewspk)
        if form.is_valid():
            form.save()
            return redirect('listFeed')
    context={'form':form}
    return render(request,'awaremeapp/feed_form.html',context)

@login_required(login_url='login')
def deleteFeed(request,pk):
    dlnewspk=OrgFeed.objects.get(id=pk)
    if request.method=='POST':
        dlnewspk.delete()
        return redirect('listFeed')
    
    context={'dlnewspk':dlnewspk}
    return render(request,'awaremeapp/delete_feed.html',context)










