from django.shortcuts import render
from django.http import HttpResponse
from . models import Description

# Create your views here.

def mypage(response):
    return render(response, "mypage/mypage.html", {'desc':Description.objects.all()})

def edit_mypage(response):

    if response.method == "POST":
        if response.POST.get("addDescription"):
            txt = response.POST.get("Description")
            if len(txt) > 10: 
                desc=Description()
                desc.txt_description=txt
                desc.save()
            else:
                print("invalid input")
                return render(response, "mypage/edit_mypage.html", {})


    return render(response, "mypage/edit_mypage.html", {})