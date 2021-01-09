from django.db import models

# Create your models here.

class Register(models.Model):
	gender_choices = [('Female','Female'),('Male','Male')]
	langs = [('C','C'),('Python','Python')]
	name=models.CharField(max_length=300)
	mobile_no=models.CharField(max_length=10)
	age=models.IntegerField()
	gender=models.CharField(max_length=30,choices=gender_choices,null=True)
	language=models.CharField(max_length=30,choices=langs,null=True)