from django.shortcuts import render,HttpResponse
from .models import *
from awaremeapp.models import OrgFeed
from django.contrib import messages

#default page

def home(request):
    feed=OrgFeed.objects.all().order_by('-id')
    context={'feed':feed,}
    return render(request,'home/home.html',context)

def aboutus(request):
    return render(request,'home/aboutus.html')

# def homeorg(request):
#     return render(request,'home/homeorg.html')

def ContactUs(request):
    
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        number=request.POST["number"]
        content=request.POST["textbox"]
        
        contact=Contact(name=name,email=email,phone=number,content=content)
        if len(name)<2 or len(email)<5 or len(content)<4 or len(number)<9:
            messages.error(request, "please fill fields properly")
        else:
            contact.save()
            messages.success(request, "response recorded successfully , you will be contacted within 24hrs")

    return render(request,'home/contact.html')


