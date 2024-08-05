from rest_framework.permissions import BasePermission, SAFE_METHODS

class CanViewDepartment(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('myapp.view_department')

class CanEditDepartment(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.has_perm('myapp.change_department')

class CanDeleteDepartment(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return request.user.has_perm('myapp.delete_department')
        return True

class CanViewEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('myapp.view_employee')

class CanEditEmployee(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.has_perm('myapp.change_employee')

class CanDeleteEmployee(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return request.user.has_perm('myapp.delete_employee')
        return True

class CanViewDeptEmp(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('myapp.view_deptemp')

class CanEditDeptEmp(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.has_perm('myapp.change_deptemp')

class CanDeleteDeptEmp(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return request.user.has_perm('myapp.delete_deptemp')
        return True

class CanViewDeptManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('myapp.view_deptmanager')

class CanEditDeptManager(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.has_perm('myapp.change_deptmanager')

class CanDeleteDeptManager(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return request.user.has_perm('myapp.delete_deptmanager')
        return True

class CanViewSalary(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('myapp.view_salary')

class CanEditSalary(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.has_perm('myapp.change_salary')

class CanDeleteSalary(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return request.user.has_perm('myapp.delete_salary')
        return True

class CanViewTitle(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('myapp.view_title')

class CanEditTitle(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.has_perm('myapp.change_title')

class CanDeleteTitle(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return request.user.has_perm('myapp.delete_title')
        return True

class CanViewPdfFile(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('myapp.view_pdffile')

class CanEditPdfFile(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.has_perm('myapp.change_pdffile')

class CanDeletePdfFile(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return request.user.has_perm('myapp.delete_pdffile')
        return True
