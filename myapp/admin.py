from django.contrib import admin
from .models import Department, Employee, DeptEmp, DeptManager, Salary, Title, PdfFile
from .forms import PdfFileForm, PDFFileInlineFormSet

class PDFFileInline(admin.TabularInline):
    model = PdfFile
    extra = 1
    formset = PDFFileInlineFormSet

class DeptEmpInline(admin.TabularInline):
    model = DeptEmp
    extra = 1

class DeptManagerInline(admin.TabularInline):
    model = DeptManager
    extra = 1

class SalaryInline(admin.TabularInline):
    model = Salary
    extra = 1

class TitleInline(admin.TabularInline):
    model = Title
    extra = 1

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_no', 'first_name', 'last_name', 'department_name', 'gender', 'hire_date')
    search_fields = ('first_name', 'emp_no', 'last_name', 'dept_no__dept_name')  
    list_filter = ('dept_no', 'gender')  
    inlines = [DeptEmpInline,PDFFileInline, DeptManagerInline, SalaryInline, TitleInline]

    def department_name(self, obj):
        return obj.dept_no.dept_name
    department_name.admin_order_field = 'dept_no'  
    department_name.short_description = 'Department Name'

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dept_no', 'dept_name')

class DeptEmpAdmin(admin.ModelAdmin):
    list_display = ('emp_no', 'dept_no', 'from_date', 'to_date')

class DeptManagerAdmin(admin.ModelAdmin):
    list_display = ('dept_no', 'emp_no', 'from_date', 'to_date')

class SalaryAdmin(admin.ModelAdmin):
    list_display = ('emp_no', 'salary', 'from_date', 'to_date')

class TitleAdmin(admin.ModelAdmin):
    list_display = ('emp_no', 'title', 'from_date', 'to_date')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(DeptEmp, DeptEmpAdmin)
admin.site.register(DeptManager, DeptManagerAdmin)
admin.site.register(Salary, SalaryAdmin)
admin.site.register(Title, TitleAdmin)

'''
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_no', 'first_name', 'last_name', 'department_name', 'gender', 'hire_date')
    search_fields = ('first_name', 'emp_no','last_name', 'dept_no__dept_name')  
    list_filter = ('dept_no', 'gender')  

    def department_name(self, obj):
        return obj.dept_no.dept_name
    department_name.admin_order_field = 'dept_no'  
    department_name.short_description = 'Department Name'

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dept_no', 'dept_name')

class DeptEmpAdmin(admin.ModelAdmin):
    list_display = ('emp_no', 'dept_no', 'from_date', 'to_date')

class DeptManagerAdmin(admin.ModelAdmin):
    list_display = ('dept_no', 'emp_no', 'from_date', 'to_date')

class SalaryAdmin(admin.ModelAdmin):
    list_display = ('emp_no', 'salary', 'from_date', 'to_date')

class TitleAdmin(admin.ModelAdmin):
    list_display = ('emp_no', 'title', 'from_date', 'to_date')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(DeptEmp, DeptEmpAdmin)
admin.site.register(DeptManager, DeptManagerAdmin)
admin.site.register(Salary, SalaryAdmin)
admin.site.register(Title, TitleAdmin)
'''