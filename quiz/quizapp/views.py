from django.shortcuts import render , redirect
from .forms import UserRegisterForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def home(request):
    return render(request, 'quizapp/index.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request, f'account created for {username}')
            return redirect('/')
    else :
        form = UserRegisterForm()
    return render(request, 'quizapp/register.html', {"form":form})
