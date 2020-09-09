from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from .signals import *
# Create your views here.
def index(request):
	return render(request,'apps/index.html')


def RegisterAdmin(request):
	context={}
	if request.POST:
		form=CreateAdminForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			rawpassword=form.cleaned_data.get('password1')
			account=authenticate(username=username,password=rawpassword)
			admin_group=Group.objects.get_or_create(name='ADMIN')
			admin_group[0].user_set.add(account)
			
	else:
		form=CreateAdminForm()
		context['CreateAdminForm']=form
	return render(request,'apps/adminregister.html',context)
	
def AdminLogin(request):
	if request.user.is_authenticated:
		redirect('index')
	context={}
	if request.POST:
		username=request.POST['username']
		rawpassword=request.POST['password']
		user=authenticate(username=username,password=rawpassword)
		if user:
			login(request,user)
			return redirect('admin_dash')
		else:
			form=AuthenticationForm(request.POST)
			context['form']=form
			return render(request,'apps/adminlogin.html',context)
	else:
		form=AuthenticationForm()
		context['form']=form
		return render(request,'apps/adminlogin.html',context)

def RegisterManager(request):
	context={}
	if request.POST:
		form1=UserForm(request.POST)
		form2=CreateManagerForm(request.POST)
		if form1.is_valid() and form2.is_valid():
			user=form1.save(commit=False)
			user.is_manager=True
			user.save()
			user.manager.mobile=form2.cleaned_data.get('mobile')
			user.manager.save()
			manager_group=Group.objects.get_or_create(name='MANAGER')
			manager_group[0].user_set.add(user)
			login(request,user)
			return redirect('manager_dash')
		else:
			context={'form1':form1,'form2':form2}
	
	else:
		form1=UserForm()
		form2=CreateManagerForm()
		context={'form1':form1,'form2':form2}
	return render(request,'apps/managerregister.html',context)

def ManagerLogin(request):
	if request.user.is_authenticated:
		redirect('manager_dash')
	context={}
	if request.POST:
		username=request.POST['username']
		rawpassword=request.POST['password']
		user=authenticate(username=username,password=rawpassword)
		if user:
			login(request,user)
			return redirect('manager_dash')
		else:
			form=AuthenticationForm(request.POST)
			context['form']=form
			return render(request,'apps/managerlogin.html',context)
	else:
		form=AuthenticationForm()
		context['form']=form
		return render(request,'apps/managerlogin.html',context)

def RegisterEmployee(request):
	context={}
	if request.POST:
		form1=UserForm(request.POST)
		form2=CreateEmployeeForm(request.POST)
		if form1.is_valid() and form2.is_valid():
			user=form1.save(commit=False)
			user.is_employee=True

			user.save()
			user.employee.mobile=form2.cleaned_data.get('mobile')
			user.employee.manager=form2.cleaned_data.get('manager')
			user.employee.save()
			employee_group=Group.objects.get_or_create(name='EMPLOYEE')
			employee_group[0].user_set.add(user)
			login(request,user)
			return redirect('employee_dash')
		else:
			context={'form1':form1,'form2':form2}
	
	else:
		form1=UserForm()
		form2=CreateEmployeeForm()
		context={'form1':form1,'form2':form2}
	return render(request,'apps/employeeregister.html',context)

def EmployeeLogin(request):
	if request.user.is_authenticated:
		return redirect('employee_dash')
	context={}
	if request.POST:
		username=request.POST['username']
		rawpassword=request.POST['password']
		user=authenticate(username=username,password=rawpassword)
		if user:
			login(request,user)
			return redirect('employee_dash')
		else:
			form=AuthenticationForm(request.POST)
			context['form']=form
			return render(request,'apps/employeelogin.html',context)
	else:
		form=AuthenticationForm()
		context['form']=form
		return render(request,'apps/employeelogin.html',context)
@login_required(login_url='login_employee')
def CreateApplication(request):
	context={}
	employee = Employee.objects.filter(user=request.user).first()
	if request.POST:
		form=CreateApplicationForm(request.POST)
		if form.is_valid():
			
			form.instance.employee=employee
			form.save()
			return render(request,'apps/employee_dash.html')
		else:
			context['form']=form
	else:
		form=CreateApplicationForm()
		context['form']=form
	return render(request,'apps/create_app.html',context)

def Admin_dash(request):
	app = Application.objects.all()
	app1 = Application.objects.filter(id=request.POST.get('answer')).all()
	for items in app1:
		items.status = request.POST.get('status')
		items.save()
	context = { 'app':app }
	return render(request,'apps/manager_dash.html',context)

def Manager_dash(request):
	manager = Manager.objects.filter(user=request.user).first()
	app = Application.objects.filter(to_manager = manager).all()
	app1 = Application.objects.filter(id=request.POST.get('answer')).all()
	for items in app1:
		items.status = request.POST.get('status')
		items.save()
	context = { 'app':app }
	return render(request,'apps/manager_dash.html',context)

def Employee_dash(request):
	employee = Employee.objects.filter(user=request.user).first()
	app = Application.objects.filter(employee=employee).all()
	context = { 'app':app }
	return render(request,'apps/employee_dash.html',context)

def StatusOfApp(request):
	employee = Employee.objects.filter(user=request.user).first()
	app = Application.objects.filter(employee=employee).all()
	context = { 'app':app }
	return render(request,'apps/employee_app_status.html',context)


def Logout_view(request):
	logout(request)
	return redirect('index')
    

