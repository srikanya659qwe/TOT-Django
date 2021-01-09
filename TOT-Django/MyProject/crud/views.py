from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
# Create your views here.
def crud(request):
	return HttpResponse("hi")
def addstudent(request):
	if request.method=="POST":
		name=request.POST['name']
		rollno=request.POST['rollno']
		age=request.POST['age']
		mobileno=request.POST['mobileno']
		email=request.POST['email']
		adress=request.POST['adress']
		gender=request.POST['gender']
		branch=request.POST['branch']
		language=request.POST.getlist('language')
		lan=""
		for la in language:
			if language.index(la)==0:
				lan+=la
			else:
				lan+=','+la
		#print(language)

		Student.objects.create(name=name,rollno=rollno,age=age,mobileno=mobileno,email=email,adress=adress,gender=gender,branch=branch,language=lan)
		#return HttpResponse("your data added successfully")
		return redirect('/crud/display')
	return render(request,'crud/addstudent.html')
def display(request):
	data=Student.objects.all()
	context={'data':data}
	return render(request,'crud/display.html',context)

def update(request,id):
	data=Student.objects.get(id=id)
	if request.method=="POST":
		name=request.POST['name']
		rollno=request.POST['rollno']
		age=request.POST['age']
		mobileno=request.POST['mobileno']
		email=request.POST['email']
		adress=request.POST['adress']
		gender=request.POST['gender']
		branch=request.POST['branch']
		language=request.POST.getlist('language')
		lan=""
		for la in language:
			if language.index(la)==0:
				lan+=la
			else:
				lan+=','+la
		data.name=name
		data.rollno=rollno
		data.age=age
		data.mobileno=mobileno
		data.email=email
		data.adress=adress
		data.gender=gender
		data.branch=branch
		data.language=lan
		data.save()
		#return HttpResponse("successfully updated")
		return redirect('/crud/display')
	return render(request,'crud/edit.html',{'mydata':data})

def delete(request,name):
	data=Student.objects.get(name=name)
	if request.method=="POST":
		data.delete()
		return redirect('/crud/display')
	return render(request,'crud/delete.html',{'mydata':data})

