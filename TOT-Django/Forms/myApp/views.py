from django.shortcuts import render,redirect
from myApp.forms import DynamicHtml
from django.http import HttpResponse
from myApp.forms import DynamicHtml,RegisterForm
from myApp.models import Register
# Create your views here.
def dynamic(request):
	if request.method=='POST':
		form=DynamicHtml(request.POST)
		#form.save()
		return render(request,'myApp/details.html',{'new':form})
	else:
		form=DynamicHtml()
		return render(request,'myApp/dynamic.html',{'form':form})

def registerForm(request):
	if request.method=="POST":
		#data=request.POST
		#print(data)
		#name=data['name']
		#print(name)
		f=RegisterForm(request.POST)
		f.save()
		return HttpResponse("done")
	f=RegisterForm()
	return render(request,'myApp/register.html',{'form':f})

def fetch(request):
	data=Register.objects.all()
	return render(request,'myApp/fetch.html',{'data':data})
def nav(request):
	return render(request,'myApp/home.html')

def edit(request,id):
	data=Register.objects.get(id=id)
	if request.method=="POST":
		form=RegisterForm(request.POST,instance=data)
		if form.is_valid():
			form.save()
			return redirect('/fetch')
	form=RegisterForm(instance=data)
	return render(request,'myApp/edit.html',{'form':form,'data':data})

def delete(request,id):
	ob=Register.objects.get(id=id)
	if request.method=="POST":
		ob.delete()
		return redirect('/fetch')
	return render(request,'myApp/delete.html',{'info':ob})