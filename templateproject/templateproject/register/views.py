from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
     if request.method== 'POST':
         username= request.POST.get('username')
         password= request.POST.get('password')
         user=auth.authenticate(username=username,password=password)
         if user is not None:
             auth.login(request,user)
             return redirect('/')
         else:
             messages.info(request,"Invalid username/password")
             return redirect('login')
     return render(request,"login.html")
def register(request):
    if request.method== 'POST':
        username= request.POST.get('username')
        firstname= request.POST.get('firstname')
        lastname= request.POST.get('lastname')
        email= request.POST.get('email')
        password= request.POST.get('password')
        cpassword= request.POST.get('password1')
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username is already taken.")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email is already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
