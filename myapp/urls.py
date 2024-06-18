from django.urls import path
from .views import department_tree

urlpatterns = [
    path('departments/', department_tree, name='department_tree'),
]
