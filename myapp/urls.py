from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import DepartmentViewSet, EmployeeViewSet, DeptEmpViewSet, DeptManagerViewSet, SalaryViewSet, TitleViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'deptemp', DeptEmpViewSet)
router.register(r'deptmanagers', DeptManagerViewSet)
router.register(r'salaries', SalaryViewSet)
router.register(r'titles', TitleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create-department/', views.create_department, name='create_department'),
    path('create-employee/', views.create_employee, name='create_employee'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

