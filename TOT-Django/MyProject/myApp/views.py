from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return HttpResponse("This is HomePage")
def abts(r):
	return HttpResponse("<h2 style='background-color:green;color:white;padding:3px;margin-left:230px;margin-right:230px'>This is AboutPage</h2>")
def rc(y,n):
	return HttpResponse("<h2>Hi Welcome {}</h2>".format(n))
def table(request,num):
	data=[]
	for i in range(1,11):
		td=str(num)+"*"+str(i)+"="+str(num*i)
		data.append(td)
		print(td)
	return HttpResponse(request,data)
def task(request,num):
	j=""
	for i in range(1,11):
		j +="{}*{:02}={:02}".format(num,i,num*i)+"\n"
	print(j)
	return HttpResponse(j)
def sg(request,name,id):
	return HttpResponse("your name is :{} <br> your id is :{}".format(name,id))

def hello(request):
	return render(request,'myApp/hello.html')
def gs(request,name,id):
	return render(request,'myApp/basic.html',{'n':name,'i':id})
def sample(request):
	return render(request,'myApp/sample.html')
def login(request):
	return render(request,'myApp/login.html')
def signup(request):
	return render(request,'myApp/signup.html')