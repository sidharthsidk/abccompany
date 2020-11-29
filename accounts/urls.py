from django.urls import path
from .views import *

urlpatterns=[
    path('accounts/login/',user_login,name='user_login'),
    path('accounts/logout/',staff_logout,name='user_logout'),
   


]