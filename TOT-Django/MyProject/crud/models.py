from django.db import models

# Create your models here.
class Student(models.Model):
	name=models.CharField(max_length=30)
	rollno=models.CharField(max_length=30)
	age=models.IntegerField()
	mobileno=models.CharField(max_length=30,null=True)
	email=models.EmailField(max_length=30)
	adress=models.TextField(null=True)
	gender=models.CharField(max_length=30,null=True)
	branch=models.CharField(max_length=30,null=True)
	language=models.CharField(max_length=30,null=True)

	def __str__(self):
		return self.name+' '+self.rollno

class Employee(models.Model):
	empId=models.IntegerField()
	efname=models.CharField(max_length=30)
	elname=models.CharField(max_length=30)
	edob=models.DateField(max_length=30)
	email=models.EmailField(max_length=30)
	eadress=models.TextField(max_length=30)
	ephoto=models.ImageField(max_length=30)
	eresume=models.FileField(max_length=30)
	edesig=models.CharField(max_length=30)
	esalary=models.IntegerField()