from django import forms

gender_choices = [('Female','Female'),('Male','Male')]
langs = [('C','C'),('Python','Python')]

class DynamicHtml(forms.Form):
	name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Name','class':'Name','class':'form-control'}))
	lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Last Name','class':'Last Name','class':'form-control'}))
	age = forms.CharField(widget=forms.NumberInput(attrs={'placeholder':'Enter Age','class':'Age','class':'form-control'}))
	email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Enter Email','class':'Email','class':'form-control'}))
	pw = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password','class':'Password','class':'form-control'}))
	cpw = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter CPasword','class':'Confirm Password','class':'form-control'}))
	DOB = forms.CharField(widget=forms.DateInput(attrs={'placeholder':'Enter Dob','class':'Dob','class':'form-control'}))
	gender = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'form-check-input','type':'radio'}),choices=gender_choices)
	select_gender = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-check-input'}),choices=gender_choices)
	select_lang = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class':'form-check-input'}),choices=langs)