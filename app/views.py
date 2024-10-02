from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import *
from .models import User

# Create your views here.



class HomeView(View):
    def get(self, request):
        return render(request, 'app/index.html')

class RegisterView(View):
    def get(self, request):
        context = {
            'form': None,
            'title': 'Register'
        }
        return render(request, 'register.html', context)

    def post(self, request: WSGIRequest):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("ro'yxatdan o'tdin")
            return redirect('home')
        messages.error(request, f"Xatolik")
        return redirect('register')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request: WSGIRequest):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')



