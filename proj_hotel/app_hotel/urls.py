from django.urls import path
from . import views


app_name = 'app_hotel'
urlpatterns =[
    path('',views.index, name="index"),
    path('about/',views.about, name="about"),
    path('contact/',views.contact, name="contact"),
    path('elements/', views.elements, name="elements"),
    path('rooms/', views.rooms, name="rooms"),
    path('services/', views.services, name="services"),
    path('blogs/', views.blog, name="blog"),
    
]
