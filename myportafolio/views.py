from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout

def index(request):
    return render(request,"pages/index.html",{})

def login(request):
    return render(request, 'pages/login.html')

@login_required
def resume(request):
    return render(request,"pages/resume.html",{})

def exit(request):
    logout(request)
    return redirect('inicio')

