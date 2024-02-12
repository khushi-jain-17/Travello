from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 
from .forms import SignUpForm
from .models import Destination

def register_user(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"you have been successfully registerd ")
            return redirect('login_user')
    else:
        form=SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})  

def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been logged in")
            return redirect('/')
        else:
            messages.success(request,"Invalid Credentails")
    else:
        return render(request,'login.html')   

def logout_user(request):
    logout(request)
    messages.success(request,"You Have Been Logged Out..")
    return redirect('login_user')           

def index(request):
    dests=Destination.objects.all()
    return render(request,'index.html',{'dests':dests})
    


