from django.urls import path
from apps.views import *
urlpatterns = [
    path('register_admin/',RegisterAdmin,name='register_admin'),
    path('login_admin/',AdminLogin,name='login_admin'),
    path('admin_dash/',Admin_dash,name='admin_dash'),
    path('register_manager/',RegisterManager,name='register_manager'),
    path('login_manager/',ManagerLogin,name='login_manager'),
    path('manager_dash/',Manager_dash,name='manager_dash'),
    path('register_employee/',RegisterEmployee,name='register_employee'),
    path('login_employee/',EmployeeLogin,name='login_employee'),
    path('employee_dash/',Employee_dash,name='employee_dash'),
    path('app_status/',StatusOfApp,name='app_status'),
    path('create_app/',CreateApplication,name='create_app'),
    path('log_out/',Logout_view,name='log_out'),
]