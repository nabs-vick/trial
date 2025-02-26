from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        
        # to check if username exists
        if User.objects.filter(username=username).exists():
            messages.error(request,"user exists")
            return redirect('accounts:login')
        
        
        # to check if password are same
        elif pass1 != pass2:
            messages.error(request,'password does not match')
            return redirect('accounts:register')
        
        
        else:
            user =User.objects.create_user(username=username, password=pass1)
            user.save()
            messages.success(request,"account created")
            return redirect('accounts:login')
    return render(request,'register.html')
        
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request,"login successful")
            return redirect('app_hotel:index')
        else:
            messages.error(request, "invalidusername or password")
            return redirect('accounts:register')
            
    return render(request,'login.html')
# def logout_view(request):
    