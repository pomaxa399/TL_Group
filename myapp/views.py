from django.shortcuts import render
from .models import Department


def department_tree(request):
    departments = Department.objects.all()
    return render(request, 'department_tree.html', {'departments': departments})
