from django.shortcuts import render, redirect
from .forms import UserRegisterForm, BookForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
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
    return render(request, 'users/register.html', {"form":form})


def addbook(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        print("hello")
        if form.is_valid():
            print("hello21")
            form.save()
            print("hello 23")
            book = form.cleaned_data.get('name')
            print("hello 24")
            messages.success(request, f'this book is added to database:  {book}')
            return redirect('/')

            
    else:
        form = BookForm()

    return render(request, "users/book.html", {"form": form})

@login_required()
def profile(request):
    return render(request, 'users/profile.html')