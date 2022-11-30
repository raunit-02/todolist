from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *

def t_sign_up(request):
    if request.user.is_authenticated:
        return redirect('/todolist')
    else:
        if request.method == 'POST':
            if request.POST['nPassword1'].strip() == request.POST['nPassword2'].strip():
                user = User(password=make_password(request.POST['nPassword1'].strip()),
                            username=request.POST['nEmail'],
                            email=request.POST['nEmail'])
                user.save()
                return redirect('userauth:login')
            else:
                context = {
                    'msg': 'Error in the inputs given, kindly make sure that you are using proper details to create user'
                }
                return render(request, 'signup.html', context)
        context = {
            'msg': ''
        }
        return render(request, 'signup.html', context)


def t_login(request):
	if request.user.is_authenticated:
		return redirect('/todolist')
	else:
		if request.method == 'POST':
			Email = request.POST.get('email_address')
			password =request.POST.get('password')
			user = authenticate(request, username=Email, password=password)

			if user is not None:
				login(request, user)
				if 'next' in request.POST:
					return redirect(request.POST.get('next'))
				else:
					return redirect('todo:todolist')
			else:
				print('Login is not success')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('/login')