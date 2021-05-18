from django.shortcuts import render,HttpResponse,redirect

from django.contrib.auth.models import User 

from django.contrib import messages

from awaremeapp.decorators import *

#user home page

@unauthenticated_user 
def userhome(request):

    if request.method == 'POST':

        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if len(username)>10:
            messages.error(request,"username should be less than 10 characters")
            return redirect('userhome')

        if not username.isalnum():
            messages.error(request,"username should only contain letters and numbers ")
            return redirect('userhome')
        
        if pass1!=pass2:
            messages.error(request,"password doesn't match ")
            return redirect('userhome')

        else:
            myuser=User.objects.create_user(username, email, pass1)
            myuser.first_name=fname
            myuser.last_name=lname
            myuser.save()
            messages.success(request,"sign up successfull")
            
            return redirect('userhome')



    else:
        return render(request,'useram/userhome.html')
        
