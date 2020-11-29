from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def user_login(request):
    if request.method == "GET":
        return render(request, 'login.html', {'form': AuthenticationForm()})

    # If POST
    lf = AuthenticationForm(data=request.POST)
    if lf.is_valid():
        username = lf.cleaned_data['username']
        password = lf.cleaned_data['password']

        user = authenticate(request, username=username, password=password)
        login(request, user)
        if user.is_superuser:
            pass
        return redirect('staff_home')

    # If invalid
    return render(request, 'login.html', {'form': lf})

def staff_logout(request):
    logout(request)
    return redirect('home')





