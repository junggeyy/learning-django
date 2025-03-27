from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from . forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required

def homepage(request):
    
    return render(request, 'authenticate/homepage.html')


def login_user(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
        
            else:
                messages.success(request, ("There was an error logging in, Try again..."))
                return redirect('login')

    context = {'loginform': form}
    return render(request, 'authenticate/login.html', context=context)
    
def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    context = {'registerform': form}
    
    return render(request, 'authenticate/register.html', context=context)

@login_required(login_url="login")
def dashboard(request):
    
    return render(request, 'authenticate/dashboard.html')


def user_logout(request):
    auth.logout(request)

    return redirect("")



