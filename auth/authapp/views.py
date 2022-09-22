from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'authapp/home.html')
