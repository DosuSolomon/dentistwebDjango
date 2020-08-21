from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about.html', views.about, name="about"),
    path('contact.html', views.contact, name="contact"),
    path('pricing.html', views.pricing, name="pricing"),
    path('blog.html', views.blog, name="blog"),
    path('blog-details.html', views.blog_details, name="blog-details"),
    path('service.html', views.service, name="service"),
    path('appointment.html', views.appointment, name="appointment"),
]