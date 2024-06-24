from django.contrib.auth import authenticate
from django.core.checks import messages
from django.shortcuts import render
from django.contrib.auth.models import User
from django import forms
from django.views.decorators.http import require_POST


# Create your views here.


def index(request):
    return render(request, 'index.html')


def chatty(request):
    return render(request, 'chatty.html')


# make signup






@require_POST
def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # redirect to home page
    else:
        messages.error(request, "Username or Password is incorrect.")

        # redirect to login page



    return render(request, 'login.html')


def logout(request):
    return render(request, 'logout.html')


def home(request):
    return render(request, 'home.html')
