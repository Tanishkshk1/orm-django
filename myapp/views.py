from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render,redirect
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from django.views.generic import View
from .forms import EmployeeForm ,DepartmentForm
from .cache_utils import generate_cache_key, get_cache_data, set_cache_data
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

    def list(self, request, *args, **kwargs):
        cache_key = generate_cache_key('department_list')
        data = get_cache_data(cache_key)
        if data:
            return Response(data)
        response = super().list(request, *args, **kwargs)
        set_cache_data(cache_key, response.data)
        return response

    def retrieve(self, request, *args, **kwargs):
        cache_key = generate_cache_key('department_retrieve', *args, **kwargs)
        data = get_cache_data(cache_key)
        if data:
            return Response(data)
        response = super().retrieve(request, *args, **kwargs)
        set_cache_data(cache_key, response.data)
        return response

    def perform_create(self, serializer):
        super().perform_create(serializer)
        cache.clear()

    def perform_update(self, serializer):
        super().perform_update(serializer)
        cache.clear()

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        cache.clear()

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated, CanViewEmployee, CanEditEmployee, CanDeleteEmployee]

    def list(self,request,*args,**kwargs):
        cache_key = generate_cache_key('employee_list')
        data = get_cache_data(cache_key)
        if data:
            return Response(data)
        response = super().list(request, *args, **kwargs)
        set_cache_data(cache_key, response.data)
        return response   

    def retrieve(self, request, *args, **kwargs):
        cache_key = generate_cache_key('employee_retrieve', *args, **kwargs)
        data = get_cache_data(cache_key)
        if data:
            return Response(data)
        response = super().retrieve(request, *args, **kwargs)
        set_cache_data(cache_key, response.data)
        return response

    def perform_create(self, serializer):
        super().perform_create(serializer)
        cache.clear()

    def perform_update(self, serializer):
        super().perform_update(serializer)
        cache.clear()

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        cache.clear()     

class DeptEmpViewSet(viewsets.ModelViewSet):
    queryset = DeptEmp.objects.all()
    serializer_class = DeptEmpSerializer
    permission_classes = [IsAuthenticated, CanViewDeptEmp, CanEditDeptEmp, CanDeleteDeptEmp]

    def list(self,request,*args,**kwargs):
        cache_key = generate_cache_key('deptemp_list')
        data = get_cache_data(cache_key)
        if data:
            return Response(data)
        response = super().list(request, *args, **kwargs)
        set_cache_data(cache_key, response.data)
        return response   

    def retrieve(self, request, *args, **kwargs):
        cache_key = generate_cache_key('deptemp_retrieve', *args, **kwargs)
        data = get_cache_data(cache_key)
        if data:
            return Response(data)
        response = super().retrieve(request, *args, **kwargs)
        set_cache_data(cache_key, response.data)
        return response

    def perform_create(self, serializer):
        super().perform_create(serializer)
        cache.clear()

    def perform_update(self, serializer):
        super().perform_update(serializer)
        cache.clear()

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        cache.clear()

class DeptManagerViewSet(viewsets.ModelViewSet):
    queryset = DeptManager.objects.all()
    serializer_class = DeptManagerSerializer
    permission_classes = [IsAuthenticated, CanViewDeptManager, CanEditDeptManager, CanDeleteDeptManager]

    def list(self,request,*args,**kwargs):
        cache_key = generate_cache_key('deptmanager_list')
        data = get_cache_data(cache_key)
        if data:
            return Response(data)
        response = super().list(request, *args, **kwargs)
        set_cache_data(cache_key, response.data)
        return response   

    def retrieve(self, request, *args, **kwargs):
        cache_key = generate_cache_key('deptmanager_retrieve', *args, **kwargs)
        data = get_cache_data(cache_key)
        if data:
            return Response(data)
        response = super().retrieve(request, *args, **kwargs)
        set_cache_data(cache_key, response.data)
        return response

    def perform_create(self, serializer):
        super().perform_create(serializer)
        cache.clear()

    def perform_update(self, serializer):
        super().perform_update(serializer)
        cache.clear()

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        cache.clear()

class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    permission_classes = [IsAuthenticated, CanViewSalary, CanEditSalary, CanDeleteSalary]

    def list(self,request,*args,**kwargs):
        cache_key = generate_cache_key('salary_list')
        data = get_cache_data(cache_key)
        if data:
            return Response(data)
        response = super().list(request, *args, **kwargs)
        set_cache_data(cache_key, response.data)
        return response   

    def retrieve(self, request, *args, **kwargs):
        cache_key = generate_cache_key('salary_retrieve', *args, **kwargs)
        data = get_cache_data(cache_key)
        if data:
            return Response(data)
        response = super().retrieve(request, *args, **kwargs)
        set_cache_data(cache_key, response.data)
        return response

    def perform_create(self, serializer):
        super().perform_create(serializer)
        cache.clear()

    def perform_update(self, serializer):
        super().perform_update(serializer)
        cache.clear()

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        cache.clear()

class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [IsAuthenticated, CanViewTitle, CanEditTitle, CanDeleteTitle]

    def list(self,request,*args,**kwargs):
        cache_key = generate_cache_key('title_list')
        data = get_cache_data(cache_key)
        if data:
            return Response(data)
        response = super().list(request, *args, **kwargs)
        set_cache_data(cache_key, response.data)
        return response   

    def retrieve(self, request, *args, **kwargs):
        cache_key = generate_cache_key('title_retrieve', *args, **kwargs)
        data = get_cache_data(cache_key)
        if data:
            return Response(data)
        response = super().retrieve(request, *args, **kwargs)
        set_cache_data(cache_key, response.data)
        return response

    def perform_create(self, serializer):
        super().perform_create(serializer)
        cache.clear()

    def perform_update(self, serializer):
        super().perform_update(serializer)
        cache.clear()

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        cache.clear()
