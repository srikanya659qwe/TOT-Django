from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Upd


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

class Updtl(forms.ModelForm):
	class Meta:
		model=User
		fields=["username","first_name","last_name","email"]
		widgets={
		"username":forms.TextInput(attrs={
			"class":"form-control",
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update FirstName",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update LastName",
			}),
		"email":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update Email",
			}),
		}


class ImPfl(forms.ModelForm):
	class Meta:
		model=Upd
		fields=["age","gender"]

		widgets={
		"age":forms.NumberInput(attrs={
			"class":"form-control",
			}),
		"gender":forms.Select(attrs={
			"class":"form-control",
			}),
		}
