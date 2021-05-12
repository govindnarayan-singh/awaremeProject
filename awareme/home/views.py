from django.shortcuts import render,HttpResponse
from .models import *
from django.contrib import messages

#default page
def home(request):
    return render(request,'home/home.html')

def homeexp(request):
    return render(request,'home/homeexp.html')

def aboutus(request):
    return render(request,'home/aboutus.html')

def homeorg(request):
    return render(request,'home/homeorg.html')

def ContactUs(request):
    
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        number=request.POST["number"]
        content=request.POST["textbox"]
        
        contact=Contact(name=name,email=email,content=content,phone=number)
        if len(name)<2 or len(email)<5 or len(content)<4 or len(number)<9:
            messages.error(request, "please fill fields properly")
        else:
            contact.save()
            messages.success(request, "response recorded successfully , you will be contacted within 24hrs")

    return render(request,'home/contact.html')


