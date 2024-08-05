from django.db import models

class Department(models.Model):
    dept_no = models.CharField(max_length=255,primary_key=True)
    dept_name = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.dept_name

class Employee(models.Model):
    emp_no = models.AutoField(primary_key=True)
    dept_no = models.ForeignKey(Department, on_delete=models.CASCADE)
    birth_date = models.DateField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1,choices=[('M','Male'),('F','Female')])
    hire_date = models.DateField()
    pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class PdfFile(models.Model):
    employee = models.ForeignKey(Employee,related_name='pdf_files',on_delete=models.CASCADE)
    file = models.FileField(upload_to='pdfs/')
    description = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return f'{self.description or "PDF File"} for {self.employee}'
        
class DeptEmp(models.Model):
    emp_no = models.ForeignKey(Employee,on_delete=models.CASCADE)
    dept_no = models.ForeignKey(Department,on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        unique_together = (('emp_no','dept_no'),)

class DeptManager(models.Model):
    dept_no = models.ForeignKey(Department,on_delete=models.CASCADE)
    emp_no = models.ForeignKey(Employee,on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        unique_together = (('dept_no','emp_no'),)

class Salary(models.Model):
    emp_no = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        unique_together = (('emp_no', 'from_date'),)

class Title(models.Model):
    emp_no = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        unique_together = (('emp_no', 'title', 'from_date'),)
