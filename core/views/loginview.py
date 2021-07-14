from django.http import HttpResponse
from django.shortcuts import render
import requests


def home(request):
    return render(request, 'static.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def
