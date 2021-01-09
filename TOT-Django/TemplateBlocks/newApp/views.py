from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Usreg,Updtl,ImPfl
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Upd
from TemplateBlocks import settings
from django.core.mail import send_mail

def home(request):
	return render(request,'newApp/home.html')
def about(request):
	return render(request,'newApp/about.html')
def contact(request):
	return render(request,'newApp/contact.html')
def register(request):
	if request.method=="POST":
		form=Usreg(request.POST)
		if form.is_valid():
			form.save()
			print(form)
			messages.success(request,"Hi you are successfully registerd")
			return redirect('/login')
	form=Usreg()
	return render(request,'newApp/register.html',{'form':form})

def dash(request):
	return render(request,'newApp/dash.html')

@login_required
def profile(request):
	return render(request,'newApp/profile.html')
@login_required
def up(request):
	if request.method=="POST":
		c=Updtl(request.POST,instance=request.user)
		y=ImPfl(request.POST,request.FILES,instance=request.user.upd)
		if c.is_valid() and y.is_valid():
			c.save()
			y.save()
			messages.success(request,"{} your details updated successfully".format(request.user.username))
			return redirect("/profile")
	c=Updtl(instance=request.user)
	y=ImPfl(instance=request.user.upd)
	return render(request,'newApp/update.html',{'c':c,'y':y})
@login_required
def mail(request):
	if request.method=="POST":
		rcv=request.POST['rcv'].split(",")
		sub=request.POST['sub']
		msg=request.POST['msg']
		snd=settings.EMAIL_HOST_USER
		t=send_mail(sub,msg,snd,[rcv])
		if t==1:
			messages.success(request,"mail send to {} successfully".format(rcv))
			return redirect("/dash")
		messages.warning(request,"mail does not send bcs of invalid mailid {}".format(rcv))
	return render(request,'newApp/mail.html')

def bus(request):
	return render(request,'newApp/bus.html')