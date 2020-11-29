from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('viewpost/<int:id>',viewpost,name='viewpost'),
]