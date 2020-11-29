from django.urls import path
from .views import *

urlpatterns=[
    path('staff/home/',staff_home,name='staff_home'),
    path('create/employe/',create_emp,name='create'),
]