"""MyProject URL Configuration

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
from myApp import views
from Boot import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('abt/',views.abts),
    path('rcd/<str:n>/',views.rc),
    path('table/<int:num>/',views.table,name='table'),
    path('task/<int:num>/',views.task,name='task'),
    path('sg/<str:name>/<int:id>/',views.sg,name='sg'),
    path('hello/',views.hello,name='hello'),
    path('ls/<str:name>/<int:id>/',views.gs,name='sg'),
    path('sample/',views.sample,name='sample'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('jsc/',views.jsc,name='jsc'),
    path('arth/',views.arth,name='arth'),
    path('second/',views.second,name='second'),
    path('ar/',views.ar,name='ar'),
    path('home/',views.home,name='home'),
    path('',v.first),
    path('boot/',views.boot,name='boot'),
    path('reg/',views.reg,name='reg'),

   


]
