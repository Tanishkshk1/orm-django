from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.views.generic import View
from .forms import EmployeeForm ,DepartmentForm
from .models import Department, Employee, DeptEmp, DeptManager, Salary, Title
from .serializers import DepartmentSerializer, EmployeeSerializer, DeptEmpSerializer, DeptManagerSerializer, SalarySerializer, TitleSerializer
from myapp.permissions import (CanViewDepartment, CanEditDepartment, CanDeleteDepartment,
                                CanViewEmployee, CanEditEmployee, CanDeleteEmployee,
                                CanViewDeptEmp, CanEditDeptEmp, CanDeleteDeptEmp,
                                CanViewDeptManager, CanEditDeptManager, CanDeleteDeptManager,
                                CanViewSalary, CanEditSalary, CanDeleteSalary,
                                CanViewTitle, CanEditTitle, CanDeleteTitle,
                                CanViewPdfFile, CanEditPdfFile, CanDeletePdfFile)

def create_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/create-employee")
    else:
        form = DepartmentForm()
    return render(request, 'index.html', {'form': form})

def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()  
    else:
        form = EmployeeForm()
    return render(request, 'index2.html', {'form': form})

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated, CanViewDepartment, CanEditDepartment, CanDeleteDepartment]

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated, CanViewEmployee, CanEditEmployee, CanDeleteEmployee]


class DeptEmpViewSet(viewsets.ModelViewSet):
    queryset = DeptEmp.objects.all()
    serializer_class = DeptEmpSerializer
    permission_classes = [IsAuthenticated, CanViewDeptEmp, CanEditDeptEmp, CanDeleteDeptEmp]

class DeptManagerViewSet(viewsets.ModelViewSet):
    queryset = DeptManager.objects.all()
    serializer_class = DeptManagerSerializer
    permission_classes = [IsAuthenticated, CanViewDeptManager, CanEditDeptManager, CanDeleteDeptManager]

class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    permission_classes = [IsAuthenticated, CanViewSalary, CanEditSalary, CanDeleteSalary]

class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [IsAuthenticated, CanViewTitle, CanEditTitle, CanDeleteTitle]
