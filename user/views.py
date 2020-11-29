from django.shortcuts import render,HttpResponse
from staff.models import EmployeCreation
from django.http.response import HttpResponseNotFound,HttpResponseBadRequest

def home(request):
    emps1=EmployeCreation.objects.all()[:100]
    return render(request,'user_home.html', {'data':emps1})

def viewpost(request, id):
    emps3 = EmployeCreation.objects.get(pk=id)
    return render(request, 'user_view_emp.html', {'data': emps3})