from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class User(AbstractUser):
	is_manager=models.BooleanField(default=False)
	is_employee=models.BooleanField(default=False)

class Manager(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	mobile=models.CharField(max_length=10,null=False)
	date_joined=models.DateTimeField(auto_now_add=True,verbose_name='date_joined')
	last_login=models.DateTimeField(auto_now=True,verbose_name='last_login')

	def __str__(self):
		return self.user.username
	
	

class Employee(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	manager = models.ForeignKey(Manager,on_delete=models.CASCADE, null=True)
	mobile=models.CharField(max_length=10,null=False)
	date_joined=models.DateTimeField(auto_now_add=True,verbose_name='date_joined')
	last_login=models.DateTimeField(auto_now=True,verbose_name='last_login')

	def __str__(self):                                                                                                                                                      
		return self.user.username
	

class Application(models.Model):
	employee=models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
	to_manager = models.ForeignKey(Manager,on_delete=models.CASCADE,null=True)
	title=models.CharField(max_length=100,null=False,blank=False)
	description=models.TextField(max_length=500,null=False,blank=False)
	start_date=models.DateTimeField(null=False,verbose_name='start_date')
	end_date=models.DateTimeField(null=False,verbose_name='end_date')
	status = models.CharField(max_length=100,null=True)

	def __str__(self):
		return self.title



