from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class Usreg(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control",
		"placeholder":"Enter password"
		}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control",
		"placeholder":"Enter confirm password"
		}))
	class Meta:
		model=User
		fields=['username']
		widgets={
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter username",
			"required":True,
			})
		}
