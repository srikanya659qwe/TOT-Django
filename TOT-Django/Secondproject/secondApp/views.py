from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Emp,Sample
# Create your views here.
def first(request):
	return HttpResponse("Hi")
def addemp(request):
	if request.method=="POST":
		eid=request.POST['eid']
		ename=request.POST['ename']
		edept=request.POST['edept']
		esalary=request.POST['esalary']
		Emp.objects.create(eid=eid,ename=ename,edept=edept,esalary=esalary)
		return HttpResponse("your data added successfully")
	return render(request,'secondApp/addemp.html')
def display(request):
	data=Emp.objects.all()
	context={'data':data}
	return render(request,'secondApp/display.html',context)

def update(request,id):
	data=Emp.objects.get(id=id)
	if request.method=="POST":
		eid=request.POST['eid']
		ename=request.POST['ename']
		edept=request.POST['edept']
		esalary=request.POST['esalary']
		data.eid=eid
		data.ename=ename
		data.edept=edept
		data.esalary=esalary
		data.save()
		return redirect('/display')

	return render(request,'secondApp/edit.html',{'mydata':data})

def delete(request,ename):
	data=Emp.objects.get(ename=ename)
	data.delete()
	return redirect('/display')

	