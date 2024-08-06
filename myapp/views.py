from rest_framework import viewsets
from django.core.cache import cache
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render,redirect
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from django.views.generic import View
from .forms import EmployeeForm ,DepartmentForm
from .cache_utils import generate_cache_key, get_cache_data, delete_cache_key, set_cache_data
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
'''
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
        cache_key = generate_cache_key('employee_list')
        cache.clear()

    def perform_update(self, serializer):
        super().perform_update(serializer)
        cache.clear()

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        cache.clear()     

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
        set_cache_data(cache_key, response.data, timeout=3600)
        return response

    def retrieve(self, request, *args, **kwargs):
        cache_key = generate_cache_key('department_retrieve', *args, **kwargs)
        data = get_cache_data(cache_key)
        if data:
            return Response(data)
        response = super().retrieve(request, *args, **kwargs)
        set_cache_data(cache_key, response.data, timeout=3600)
        return response

    def perform_create(self, serializer):
        instance = serializer.save()
        cache_key = generate_cache_key('department_retrieve', instance.pk)
        set_cache_data(cache_key, DepartmentSerializer(instance).data, timeout=3600)
        cache_key_list = generate_cache_key('department_list')
        cache.delete(cache_key_list)

    def perform_update(self, serializer):
        instance = serializer.save()
        cache_key = generate_cache_key('department_retrieve', instance.pk)
        set_cache_data(cache_key, DepartmentSerializer(instance).data, timeout=3600)
        cache_key_list = generate_cache_key('department_list')
        cache.delete(cache_key_list)

    def perform_destroy(self, instance):
        instance.delete()
        cache_key = generate_cache_key('department_retrieve', instance.pk)
        cache.delete(cache_key)
        cache_key_list = generate_cache_key('department_list')
        cache.delete(cache_key_list)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated, CanViewEmployee, CanEditEmployee, CanDeleteEmployee]

    def list(self, request, *args, **kwargs):
        cache_key = generate_cache_key('employee_list')
        data = get_cache_data(cache_key)
        if data:
            return Response(data)
        response = super().list(request, *args, **kwargs)
        set_cache_data(cache_key, response.data, timeout=3600)
        return response

    def retrieve(self, request, *args, **kwargs):
        cache_key = generate_cache_key('employee_retrieve', *args, **kwargs)
        data = get_cache_data(cache_key)
        if data:
            return Response(data)
        response = super().retrieve(request, *args, **kwargs)
        set_cache_data(cache_key, response.data, timeout=3600)
        return response

    def perform_create(self, serializer):
        instance = serializer.save()
        cache_key = generate_cache_key('employee_retrieve', instance.pk)
        set_cache_data(cache_key, EmployeeSerializer(instance).data, timeout=3600)
        cache_key_list = generate_cache_key('employee_list')
        cache.delete(cache_key_list)

    def perform_update(self, serializer):
        instance = serializer.save()
        cache_key = generate_cache_key('employee_retrieve', instance.pk)
        set_cache_data(cache_key, EmployeeSerializer(instance).data, timeout=3600)
        cache_key_list = generate_cache_key('employee_list')
        cache.delete(cache_key_list)

    def perform_destroy(self, instance):
        instance.delete()
        cache_key = generate_cache_key('employee_retrieve', instance.pk)
        cache.delete(cache_key)
        cache_key_list = generate_cache_key('employee_list')
        cache.delete(cache_key_list)

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
'''

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
        instance = serializer.save()
        cache_key = generate_cache_key('department_retrieve', instance.pk)
        set_cache_data(cache_key, DepartmentSerializer(instance).data)
        cache_key_list = generate_cache_key('department_list')
        delete_cache_key(cache_key_list)

    def perform_update(self, serializer):
        instance = serializer.save()
        cache_key = generate_cache_key('department_retrieve', instance.pk)
        set_cache_data(cache_key, DepartmentSerializer(instance).data)
        cache_key_list = generate_cache_key('department_list')
        delete_cache_key(cache_key_list)

    def perform_destroy(self, instance):
        instance.delete()
        cache_key = generate_cache_key('department_retrieve', instance.pk)
        delete_cache_key(cache_key)
        cache_key_list = generate_cache_key('department_list')
        delete_cache_key(cache_key_list)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated, CanViewEmployee, CanEditEmployee, CanDeleteEmployee]

    def list(self, request, *args, **kwargs):
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
        instance = serializer.save()
        cache_key = generate_cache_key('employee_retrieve', instance.pk)
        set_cache_data(cache_key, EmployeeSerializer(instance).data)
        cache_key_list = generate_cache_key('employee_list')
        delete_cache_key(cache_key_list)

    def perform_update(self, serializer):
        instance = serializer.save()
        cache_key = generate_cache_key('employee_retrieve', instance.pk)
        set_cache_data(cache_key, EmployeeSerializer(instance).data)
        cache_key_list = generate_cache_key('employee_list')
        delete_cache_key(cache_key_list)

    def perform_destroy(self, instance):
        instance.delete()
        cache_key = generate_cache_key('employee_retrieve', instance.pk)
        delete_cache_key(cache_key)
        cache_key_list = generate_cache_key('employee_list')
        delete_cache_key(cache_key_list)

class DeptEmpViewSet(viewsets.ModelViewSet):
    queryset = DeptEmp.objects.all()
    serializer_class = DeptEmpSerializer
    permission_classes = [IsAuthenticated, CanViewDeptEmp, CanEditDeptEmp, CanDeleteDeptEmp]

    def list(self, request, *args, **kwargs):
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
        instance = serializer.save()
        cache_key = generate_cache_key('deptemp_retrieve', instance.pk)
        set_cache_data(cache_key, DeptEmpSerializer(instance).data)
        cache_key_list = generate_cache_key('deptemp_list')
        delete_cache_key(cache_key_list)

    def perform_update(self, serializer):
        instance = serializer.save()
        cache_key = generate_cache_key('deptemp_retrieve', instance.pk)
        set_cache_data(cache_key, DeptEmpSerializer(instance).data)
        cache_key_list = generate_cache_key('deptemp_list')
        delete_cache_key(cache_key_list)

    def perform_destroy(self, instance):
        instance.delete()
        cache_key = generate_cache_key('deptemp_retrieve', instance.pk)
        delete_cache_key(cache_key)
        cache_key_list = generate_cache_key('deptemp_list')
        delete_cache_key(cache_key_list)

class DeptManagerViewSet(viewsets.ModelViewSet):
    queryset = DeptManager.objects.all()
    serializer_class = DeptManagerSerializer
    permission_classes = [IsAuthenticated, CanViewDeptManager, CanEditDeptManager, CanDeleteDeptManager]

    def list(self, request, *args, **kwargs):
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
        instance = serializer.save()
        cache_key = generate_cache_key('deptmanager_retrieve', instance.pk)
        set_cache_data(cache_key, DeptManagerSerializer(instance).data)
        cache_key_list = generate_cache_key('deptmanager_list')
        delete_cache_key(cache_key_list)

    def perform_update(self, serializer):
        instance = serializer.save()
        cache_key = generate_cache_key('deptmanager_retrieve', instance.pk)
        set_cache_data(cache_key, DeptManagerSerializer(instance).data)
        cache_key_list = generate_cache_key('deptmanager_list')
        delete_cache_key(cache_key_list)

    def perform_destroy(self, instance):
        instance.delete()
        cache_key = generate_cache_key('deptmanager_retrieve', instance.pk)
        delete_cache_key(cache_key)
        cache_key_list = generate_cache_key('deptmanager_list')
        delete_cache_key(cache_key_list)

class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    permission_classes = [IsAuthenticated, CanViewSalary, CanEditSalary, CanDeleteSalary]

    def list(self, request, *args, **kwargs):
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
        instance = serializer.save()
        cache_key = generate_cache_key('salary_retrieve', instance.pk)
        set_cache_data(cache_key, SalarySerializer(instance).data)
        cache_key_list = generate_cache_key('salary_list')
        delete_cache_key(cache_key_list)

    def perform_update(self, serializer):
        instance = serializer.save()
        cache_key = generate_cache_key('salary_retrieve', instance.pk)
        set_cache_data(cache_key, SalarySerializer(instance).data)
        cache_key_list = generate_cache_key('salary_list')
        delete_cache_key(cache_key_list)

    def perform_destroy(self, instance):
        instance.delete()
        cache_key = generate_cache_key('salary_retrieve', instance.pk)
        delete_cache_key(cache_key)
        cache_key_list = generate_cache_key('salary_list')
        delete_cache_key(cache_key_list)

class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [IsAuthenticated, CanViewTitle, CanEditTitle, CanDeleteTitle]

    def list(self, request, *args, **kwargs):
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
        instance = serializer.save()
        cache_key = generate_cache_key('title_retrieve', instance.pk)
        set_cache_data(cache_key, TitleSerializer(instance).data)
        cache_key_list = generate_cache_key('title_list')
        delete_cache_key(cache_key_list)

    def perform_update(self, serializer):
        instance = serializer.save()
        cache_key = generate_cache_key('title_retrieve', instance.pk)
        set_cache_data(cache_key, TitleSerializer(instance).data)
        cache_key_list = generate_cache_key('title_list')
        delete_cache_key(cache_key_list)

    def perform_destroy(self, instance):
        instance.delete()
        cache_key = generate_cache_key('title_retrieve', instance.pk)
        delete_cache_key(cache_key)
        cache_key_list = generate_cache_key('title_list')
        delete_cache_key(cache_key_list)