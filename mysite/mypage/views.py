from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from . models import Description
from . forms import *
from django.db import IntegrityError

# Create your views here.

def goto_mypage(response):
    return HttpResponseRedirect('/mypage/'+response.user.get_short_name())

#@login_required(login_url='/login/')
def mypage(response, name):
    users=User.objects.all()
    for u in users:
        if u.get_username() == name:
            description=Description.objects.filter(user=u)
            gallery=Gallery.objects.filter(user=u)
            return render(response, "mypage/mypage.html", {'desc':description, 'gallery': gallery})
    return HttpResponseNotFound('<h1>Page not found</h1><h3>Is it possible that you made an error writting the name?</h3')


@login_required(login_url='/login/')
def edit_mypage(response):

    if  Description.objects.filter(user=response.user).exists() == False:
        form_desc = CreateDescription()
    else:
        default_text = Description.objects.get(user=response.user)
        form_desc = CreateDescription(initial={'txt_description': default_text})
        print("jaja")

    form_gallery = CreateGallery()
    form_delete = DeleteNamedFile()

    if response.method == "POST":
        form_desc = CreateDescription(response.POST, response.FILES)
        form_gallery = CreateGallery(response.POST, response.FILES)
        form_delete = DeleteNamedFile(response.POST)

        if form_desc.is_valid():

            txt = form_desc.cleaned_data["txt_description"]
            pic = form_desc.cleaned_data["profile_pic"]
            print(pic)

            if  Description.objects.filter(user=response.user).exists() == False:
                desc = Description(txt_description=txt, profile_pic=pic)
                desc.save()
                response.user.description.add(desc)
                return HttpResponseRedirect('/mypage/'+response.user.get_username())
            else: 
                if pic==None :
                    Description.objects.filter(user=response.user).update(txt_description=txt)
                else:
                    Description.objects.filter(user=response.user).delete() #delete old decription
                    desc = Description(txt_description=txt, profile_pic=pic) 
                    desc.save()
                    response.user.description.add(desc)
                return HttpResponseRedirect('/mypage/'+response.user.get_username())


        
        if form_gallery.is_valid():
            try:
                name = form_gallery.cleaned_data["name"]
                txt = form_gallery.cleaned_data["txt"]
                newfile = form_gallery.cleaned_data["new_file"]
                gall = Gallery(name=name, txt=txt, new_file=newfile)
                gall.save()
                response.user.gallery.add(gall)
                messages.success(response, 'Upload successful')
                return HttpResponseRedirect('/edit_mypage/')
            except IntegrityError as err:
                messages.success(response, 'A document with such a name already exists!')
                return HttpResponseRedirect('/edit_mypage/')
       
        if form_delete.is_valid():
            file_name=form_gallery.cleaned_data["name"]
            delete_file = response.user.gallery.filter(name=file_name)
            delete_file.delete()
    return render(response, "mypage/edit_mypage.html", {"form_desc":form_desc, "form_gallery":form_gallery, "form_delete":form_delete})