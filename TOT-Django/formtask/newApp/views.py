from django.shortcuts import render,redirect
from newApp.forms import DynamicHtml
from django.http import HttpResponse
# Create your views here.
def dynamic(request):
	if request.method == 'POST':
		fn=request.POST.get('name')
		ln=request.POST.get('lastname')
		a=request.POST.get('age')
		e =request.POST.get('email')
		p=request.POST.get('pw')
		cp=request.POST.get('cpw')
		d=request.POST.get('DOB')
		sg=request.POST.get('select_gender')
		sl=request.POST.get('select_lang')
		s = ''
		for lang in sl:
			if(sl.index(lang) == 0):
				s +=lang
			else:
				s+=','+lang
			return render(request,'newApp/task.html',{'name':fn,'lastname':ln,'age':a,'email':e,'pw':p,'cpw':cp,'DOB':d,'select_gender':sg,'select_lang':sl})
	t =DynamicHtml()
	return render(request,'newApp/add.html',{'form':t})
	