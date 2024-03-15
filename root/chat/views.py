from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserInfo
from .models import User
from django.contrib import messages
import requests


# Create your views here.
# def home(request):
#     f_form = CardFullForm()
#     e_form = CardEmptyForm()
#     cards = Card.objects.all().order_by('word')
#
#     return render(request, 'landing.html', {'f_form': f_form, 'e_form': e_form, 'cards': cards})


# Create your views here.
def landing(request):
    if request.method == 'GET':
        user_form = UserInfo()
        return render(request, 'landing.html', {'user_form': user_form})


def signup(request):
    user_form = UserInfo()
    return render(request, 'signup.html', {'user_form': user_form})


def signin(request):
    if request.method == 'POST':
        user_form = UserInfo(request.POST)
        print("Hello")
        if user_form.is_valid():
            print("Hello!")
            usernamed = user_form.cleaned_data['username']
            passwordd = user_form.cleaned_data['password']
            print(passwordd)
            if User.objects.filter(username=user_form.cleaned_data['username']).exists():
                user = User.objects.get(username=user_form.cleaned_data['username'])
                password = user.password
                if password == passwordd:
                    return redirect('message')  # Redirect to a success page.
                else:
                    messages.error(request, 'Invalid password.')
                    return redirect('landing')  # Redirect back to the sign-in page.
            else:
                messages.error(request, 'Username does not exist')
                return redirect('landing')

        else:
            print('hello!!!!!2222')
            return render(request, 'landing.html', {'user_form': user_form})
    else:
        user_form = UserInfo()
        print('hello!!!!!')
        return render(request, 'landing.html', {'user_form': user_form})


def adduser(request):
    if request.method == 'POST':
        form_f = UserInfo(request.POST)
        if form_f.is_valid():
            # Use get_or_create to find or create a User instance with the word from the form
            # If the user was created, save the password

            if User.objects.filter(username=form_f.cleaned_data['username']).exists():
                messages.error(request, 'Username already exists. Please choose a different username.')
                return redirect('signup')
            else:
                new_user = User(username=form_f.cleaned_data['username'], password=form_f.cleaned_data['password'])
                new_user.save()
            return redirect('landing')  # Assuming 'landing' is a valid URL name
    else:

        return render(request, 'signup.html')


def message(request):
    return render(request, 'messages.html')
