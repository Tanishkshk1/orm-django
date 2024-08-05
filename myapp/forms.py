from django import forms
from  .models import Department, Employee, DeptEmp, DeptManager, Salary, Title,PdfFile
from django.forms import BaseInlineFormSet

class CombinedEmployeeForm(forms.ModelForm):
    # Employee fields
    emp_no = forms.IntegerField()
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    dept_no = forms.ModelChoiceField(queryset=Department.objects.all())
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
    hire_date = forms.DateField()
    
    # DeptEmp fields
    dept_emp_from_date = forms.DateField()
    dept_emp_to_date = forms.DateField()
    
    # DeptManager fields
    dept_manager_from_date = forms.DateField()
    dept_manager_to_date = forms.DateField()
    
    # Salary fields
    salary_amount = forms.IntegerField()
    salary_from_date = forms.DateField()
    salary_to_date = forms.DateField()
    
    # Title fields
    title_name = forms.CharField(max_length=50)
    title_from_date = forms.DateField()
    title_to_date = forms.DateField()

    class Meta:
        model = Employee
        fields = ['emp_no', 'first_name', 'last_name', 'dept_no', 'gender', 'hire_date','pdf_file']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            dept_emp = DeptEmp.objects.filter(emp_no=self.instance)
            if dept_emp.exists():
                self.initial['dept_emp_from_date'] = dept_emp.first().from_date
                self.initial['dept_emp_to_date'] = dept_emp.first().to_date



class PdfFileForm(forms.ModelForm):
    class Meta:
        model = PdfFile
        fields = ['file', 'description']

class PDFFileInlineFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super(PDFFileInlineFormSet, self).__init__(*args, **kwargs)
        self.queryset = self.queryset.order_by('description')

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['dept_no', 'dept_name']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_no', 'dept_no', 'birth_date', 'first_name', 'last_name', 'gender', 'hire_date']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dept_no'].queryset = Department.objects.all()