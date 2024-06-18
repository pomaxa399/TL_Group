from django.contrib import admin
from .models import Employee, Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'level')
    search_fields = ('name',)
    list_filter = ('level',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'hire_date', 'salary', 'department')
    search_fields = ('name', 'position')
    list_filter = ('hire_date', 'department')
