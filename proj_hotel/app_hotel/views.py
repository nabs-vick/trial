from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about-us.html')
def contact(request):
    return render(request,'contact.html')
def blog(request):
    return render(request,'blog.html')
def elements(request):
    return render(request,'elements.html')
def rooms(request):
    return render(request,'rooms.html')
def services(request):
    return render(request,'services.html')