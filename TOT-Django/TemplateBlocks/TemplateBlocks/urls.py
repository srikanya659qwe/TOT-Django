"""TemplateBlocks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from newApp import views
from django.contrib.auth import views as v
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('reg/',views.register,name='reg'),
    path('login/',v.LoginView.as_view(template_name="newApp/login.html"),name="login"),
    path('dash/',views.dash,name='dash'),
    path('logout/',v.LogoutView.as_view(template_name="newApp/logout.html"),name="logout"),
    path('profile/',views.profile,name='profile'),
    path('up/',views.up,name='upd'),
    path('mail/',views.mail,name='mail'),
    path('bus/',views.bus,name='bus'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
