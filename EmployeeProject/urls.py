from django.contrib import admin
from django.urls import path, re_path
from EmployeeApp import views

urlpatterns = [
    re_path(r'^employee$', views.employeeApi),
    re_path(r'^employee/([0-9]+)$', views.employeeApi),
    path('admin/', admin.site.urls),
]

