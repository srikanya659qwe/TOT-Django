from django.shortcuts import render
from django.http import HttpResponse
from .forms import UsReg

# Create your views here.
def home(request):
	return render(request,'newApp/home.html')
def about(request):
	return render(request,'newApp/about.html')
def contact(request):
	return render(request,'newApp/contact.html')
def dash(request):
	return render(request,'newApp/dash.html')
def reg(request):
	if request.method == 'POST':
		y = UsReg(request.POST)
		# print(y)
		if y.is_valid():
			y.save()
			messages.success(request,"You are successfully registered..!")
			return redirect('/login')
	y = UsReg()

	return render(request,'newApp/reg.html')

