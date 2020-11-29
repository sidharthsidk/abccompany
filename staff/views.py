from django.shortcuts import render,redirect
from .models import EmployeCreation
from .forms import *
import os

# Create your views here.
def staff_home(request):
    emps = EmployeCreation.objects.all()[:100]
    return render(request, 'staff_home.html', {'data': emps})

def create_emp(request):
    if request.method == "GET":
        ec=EmployeCreationForm()
        return render(request,'create.html', {'form':ec})
    bcf = EmployeCreationForm(request.POST,request.FILES)
    if bcf.is_valid():
        bcf.save()
        return redirect('staff_home')
    
    return render(request, 'create.html', {'form': bcf})

