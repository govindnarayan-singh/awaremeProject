from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .filters import newsFilter
from .decorators import *



def index(request):
    return render(request,'awaremeapp/index.html')

@unauthenticated_user 
def orgRegister(request):
    form1=OrgUser()
    
    if request.method =='POST':
        form1=OrgUser(request.POST)

        if form1.is_valid():
            user=form1.save()
        

            group = Group.objects.get(name='NGO')
            user.groups.add(group)

            username = form1.cleaned_data.get('username')
            messages.success(request,'account created successfully with username as ' + username)
            return redirect('mission')
        else:
            print("error!")
    else:
        form1=OrgUser()
        form=Organisation()
    return render(request,'awaremeapp/registration.html',{'form1':form1,'form':form})

@unauthenticated_user
def mission(request):
    form=mission_register()
    if request.method== 'POST':
        form=mission_register(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context={'form':form}
    return render(request,'awaremeapp/register_mission.html',context)

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('index')


@unauthenticated_user 
def user_login(request):
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
    userList = User.objects.values()
    return render(request,'awaremeapp/info.html',{'model':Instance1,'userList':userList})

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
    filterNews = newsFilter(request.GET,queryset=feed)
    feed=filterNews.qs 
    context={'feed':feed,'filterNews':filterNews}
    return render(request,'awaremeapp/list_feed.html',context)



def newsFeed(request,pk):
    news=OrgFeed.objects.all()
    newspk=OrgFeed.objects.get(id=pk)
    context={'news':news,'newspk':newspk}
    return render(request,'awaremeapp/news_feed.html',context)


@allowed_user(allowed_roles=['admin','NGO'])
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


@allowed_user(allowed_roles=['admin','NGO'])
@login_required(login_url='login')
def deleteFeed(request,pk):
    dlnewspk=OrgFeed.objects.get(id=pk)
    if request.method=='POST':
        dlnewspk.delete()
        return redirect('listFeed')
    
    context={'dlnewspk':dlnewspk}
    return render(request,'awaremeapp/delete_feed.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin','NGO'])
def account_set(request):
    ngo = request.user.orgdetail
    form = Organisation(instance=ngo)
    if request.method == 'POST':
        form = Organisation(request.POST, request.FILES,instance=ngo)
        if form.is_valid():
            form.save()
            return redirect('listFeed')
    context={'form':form}
    return render(request,'awaremeapp/account_setting.html',context)












