from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group,User
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import *
from awaremeapp.templatetags import extras



#Authentication APIs
@unauthenticated_user 
def orgRegister(request):

    if request.method == 'POST':

        username=request.POST['username']
        fname=request.POST['fname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if len(username)>10:
            messages.error(request,"username should be less than 10 characters")
            return redirect('usersignup')

        if not username.isalnum():
            messages.error(request,"username should only contain letters and numbers ")
            return redirect('usersignup')
        
        if pass1!=pass2:
            messages.error(request,"password doesn't match ")
            return redirect('usersignup')

        else:
            myuser=User.objects.create_user(username, email, pass1)
            myuser.first_name=fname
            myuser.save()
            messages.success(request,"sign up successfull")
        
            group = Group.objects.get(name='NGO')
            myuser.groups.add(group)

            
            messages.success(request,'account created successfully with username as ' + username)
            return redirect('mission')
       
    else:
        return render(request,'awaremeapp/registration.html')

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
    return redirect('login')

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


#Html pages
@login_required(login_url='login')
def orgList(request):
    Instance1=OrgDetail.objects.all()
    userList = User.objects.values()
    Instance=Instance1.union(userList,all=True)
    return render(request,'awaremeapp/info.html',{'model':Instance1,'userList':userList})


@login_required(login_url='login')
def org_profile(request,pk_value):
    orgPk=OrgDetail.objects.get(id=pk_value)
    orgInfo=OrgDetail.objects.all()
    context={'orgInfo':orgInfo,'orgPk':orgPk}
    return render(request,'awaremeapp/org_profile.html',context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin','NGO'])
def createFeed(request):
    form=Formfeed()
    if request.method=='POST':
        form=Formfeed(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listFeed')
    context={'form':form}
    return render(request,'awaremeapp/feed_form.html',context)


@login_required(login_url='login')
def listFeed(request):
    feed=OrgFeed.objects.all()
    context={'feed':feed,}
    return render(request,'awaremeapp/list_feed.html',context)


@login_required(login_url='login')
def newsFeed(request,pk):
    newspk=OrgFeed.objects.get(id=pk)
    comments=FeedComment.objects.filter(post=newspk,parent=None)
    replies=FeedComment.objects.filter(post=newspk).exclude(parent=None)
    
    replyDict={}

    for reply in replies:
        if reply.id not in replyDict.keys():
            replyDict[reply.parent.id]=[reply]
        else:
            replyDict[reply.parent.id].append(reply)

    print(replyDict)
    count=comments.count()
    context={'newspk':newspk,'comments':comments,'count':count,'replyDict':replyDict}
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


@login_required(login_url='login')
def postComment(request,pk):
    if request.method=="POST":
        comment=request.POST.get("comment")
        writer=request.user
    
        post=OrgFeed.objects.get(id=pk)
        parentSno=request.POST.get("parentSno")

        if parentSno== "":
            comment=FeedComment(comment=comment,writer=writer,post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent = FeedComment.objects.get(id=parentSno)
            comment=FeedComment(comment=comment,writer=writer,post=post,parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
    
    return redirect(f'/awareme/newsFeed/{pk}')


@login_required(login_url='login')
def search(request):
    query=request.GET['query']
    if len(query) > 70:
        feed=OrgFeed.objects.none()
        

    else:
        feedtitle=OrgFeed.objects.filter(title__icontains=query)
        feedcontent=OrgFeed.objects.filter(brief__icontains=query)
        feed2=feedtitle.union(feedcontent)
        feedlocation=OrgFeed.objects.filter(locations__icontains=query)
        # feedlocation=OrgFeed.objects.filter(author__icontains=query)
        feed3=feed2.union(feedlocation)
        feed=feed3.union(feed3)


    if feed.count() == 0:
        messages.warning(request," no results found please refine your query ")


    context={'feed':feed,'query':query}
    return render(request,'awaremeapp/search.html',context)
     










