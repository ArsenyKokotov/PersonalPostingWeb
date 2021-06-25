from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from . models import Description
from . forms import *

# Create your views here.

def mypage(response):
    return render(response, "mypage/mypage.html", {'desc':Description.objects.all(), 'gallery': Gallery.objects.all()})

def edit_mypage(response):

    form_desc = CreateDescription()
    form_gallery = CreateGallery()

    if response.method == "POST":
        form_desc = CreateDescription(response.POST, response.FILES)
        form_gallery = CreateGallery(response.POST, response.FILES)

        if form_desc.is_valid():
            txt = form_desc.cleaned_data["txt_description"]
            pic= form_desc.cleaned_data["profile_pic"]
            desc = Description(txt_description=txt, profile_pic=pic)
            desc.save()
            return HttpResponseRedirect('/mypage/')
        
        if form_gallery.is_valid():
            txt = form_gallery.cleaned_data["txt"]
            newfile = form_gallery.cleaned_data["new_file"]
            gall = Gallery(txt=txt, new_file=newfile)
            gall.save()
            messages.success(response, 'Upload successful')
            return HttpResponseRedirect('/edit_mypage/')

    return render(response, "mypage/edit_mypage.html", {"form_desc":form_desc, "form_gallery":form_gallery})