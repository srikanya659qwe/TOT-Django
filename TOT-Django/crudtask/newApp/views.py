from django.shortcuts import render
from django.http import HttpResponse
from .models import Sample
# Create your views here.

def basic(request):
	return HttpResponse("hello")
def add(request):
	 if request.method == 'POST':
	 	contact = Sample(yourname=request.POST.get("yourname"),mailid=request.POST.get('mailid'),
                          subject=request.POST.get('subject'), body=request.POST.get('body'),
                          gender=request.POST.get('gender'),language=request.POST.get('language'),
                          country=request.POST.get('country'))
	 	contact.save()
	 	return HttpResponse("added data successfully")
	 return render(request,'newApp/add.html')

def display(request):
	data=Sample.objects.all()
	context={'data':data}
	return render(request,'newApp/display.html',context)
