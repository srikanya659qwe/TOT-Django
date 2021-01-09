from django import forms
from .models import Register
#from django.forms import ModelForm

class RegisterForm(forms.ModelForm):
	class Meta:
		model=Register
		fields='__all__'


		gender_choices = [('Female','Female'),('Male','Male')]
		widgets={
			"name":forms.TextInput(attrs={"placeholder":"Enter Name"}),
			"mobile_no":forms.TextInput(attrs={"placeholder":"Enter mobile number"}),
			"age":forms.NumberInput(attrs={"required":False,"placeholder":"Enter Age"}),
			"gender":forms.RadioSelect(attrs={'class':'radio-inline','type':'radio'})

			
		}









gender_choices = [('Female','Female'),('Male','Male')]
langs = [('C','C'),('Python','Python')]

class DynamicHtml(forms.Form):
	name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Name','class':'Name'}))
	lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Last Name','class':'Last Name'}))
	age = forms.CharField(widget=forms.NumberInput(attrs={'placeholder':'Enter Age','class':'Age'}))
	email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Enter Email','class':'Email'}))
	pw = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password','class':'Password'}))
	cpw = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter CPasword','class':'Confirm Password'}))
	DOB = forms.CharField(widget=forms.DateInput(attrs={'placeholder':'Enter Dob','class':'Dob'}))
	gender = forms.ChoiceField(widget=forms.RadioSelect,choices=gender_choices)
	select_gender = forms.ChoiceField(widget=forms.Select,choices=gender_choices)
	select_lang = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=langs)