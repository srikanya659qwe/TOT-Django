from django.db import models

# Create your models here.
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

	def __str__(self):
		self.empId+' '+self.efname

class Emp(models.Model):
	eid=models.IntegerField()
	ename=models.CharField(max_length=30)
	edept=models.CharField(max_length=30)
	esalary=models.FloatField()

	def __str__(self):
		return self.ename+' '+self.edept+' '+str(self.eid)+' '+str(self.esalary)

class Sample(models.Model):
	eid=models.IntegerField()
	ename=models.CharField(max_length=30)
	edept=models.CharField(max_length=30)
	esalary=models.FloatField()
	isemployee=models.BooleanField("Is Employee",default=False)
	isstudent=models.BooleanField("Is Student",default=False)
	role=(
			('user','USER'),
			('admin','ADMIN')
		)
	roles=models.CharField(max_length=10,choices=role,default="user")

	GENDER_CHOICES = (
  						 ('M', 'Male'),
   						 ('F', 'Female')
					)
	gender=models.CharField(choices=GENDER_CHOICES, max_length=128)



