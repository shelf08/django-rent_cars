from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')

def lk(request):
    return render(request, 'main/lk.html')

def signin(request):
    return render(request, 'main/signin.html')

def signup(request):
    return render(request, 'main/signup.html')
