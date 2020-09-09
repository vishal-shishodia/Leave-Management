from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class UserForm(UserCreationForm):
	class Meta:
		model=User
		fields=['first_name','last_name','username','password1']


class CreateAdminForm(UserCreationForm):
	class Meta:
		model=User
		fields=['first_name','last_name','username','password1']



class CreateManagerForm(forms.ModelForm):
	class Meta:
		model=Manager
		fields=['mobile']


class CreateEmployeeForm(forms.ModelForm):
	class Meta:
		model=Employee
		fields=['mobile','manager']

class CreateApplicationForm(forms.ModelForm):
	class Meta:
		model=Application
		fields=['title','description','start_date','end_date','to_manager']

