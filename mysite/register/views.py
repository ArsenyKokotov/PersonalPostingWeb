from django.shortcuts import render, redirect
from . forms import RegisterForm
from  mypage.models import *
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound



# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            if User.objects.filter(username=username).exists()==True:
                return render(response, "register/register.html", {"form":form})
            elif User.objects.filter(email=email).exists()==True:
                messages.success(response, 'A user with such an email already exists!')
                return HttpResponseRedirect('/register/')
            else:
                form.save()
                return redirect("/edit_mypage/")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})