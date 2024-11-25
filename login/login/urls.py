"""
URL configuration for login project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('roadmap/', views.roadmap, name='roadmap'),  # Separate view for roadmap
    path('journey/', views.journey, name='journey'),  # Separate view for journey
    path('motivation/', views.motivation, name='motivation'),  # Separate view for motivation
    path('previous/', views.previous, name='previous'),  # Separate view for previous
    path('friend/', views.friend, name='friend'),  # Separate view for friend
    path('quiz/', views.quiz, name='quiz'),  # Separate view for quiz
    path('setting/', views.setting, name='setting'),  # Separate view for setting
    path('contact/', views.contact, name='contact'),  # Separate view for contact
    path('ai/',views.ai, name='ai'),
]

