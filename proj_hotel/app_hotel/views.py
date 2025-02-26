from django.shortcuts import render, redirect
from . models import Content
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about-us.html')
@login_required
def contact(request):
    if request.method == 'POST':
        components = Content(
            username = request.POST['username'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],
        )
        components.save()
        messages.success(request,'thank you for the info')
        return redirect('app_hotel:index')
    else:
        messages.error(request,"error in submition")
        return render(request,'contact.html')
def blog(request):
    return render(request,'blog.html')
def elements(request):
    return render(request,'elements.html')
def rooms(request):
    return render(request,'rooms.html')
def services(request):
    return render(request,'services.html')