from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from . models import Description
from . forms import *

# Create your views here.

def goto_mypage(response):
    return HttpResponseRedirect('/mypage/'+response.user.get_short_name())

#@login_required(login_url='/login/')
def mypage(response, name):
    users=User.objects.all()
    for u in users:
        if u.get_short_name() == name:
            description=Description.objects.filter(user=u)
            gallery=Gallery.objects.filter(user=u)
            return render(response, "mypage/mypage.html", {'desc':description, 'gallery': gallery})
            break
    return HttpResponseNotFound('<h1>Page not found</h1><h3>Is it possible that you made an error writting the name?</h3')


@login_required(login_url='/login/')
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
            response.user.description.add(desc)
            return HttpResponseRedirect('/mypage/'+response.user.get_short_name())
        
        if form_gallery.is_valid():
            txt = form_gallery.cleaned_data["txt"]
            newfile = form_gallery.cleaned_data["new_file"]
            gall = Gallery(txt=txt, new_file=newfile)
            gall.save()
            response.user.gallery.add(gall)
            messages.success(response, 'Upload successful')
            return HttpResponseRedirect('/edit_mypage/')

    return render(response, "mypage/edit_mypage.html", {"form_desc":form_desc, "form_gallery":form_gallery})