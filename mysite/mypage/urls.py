#creating url paths

from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path("goto_mypage", views.goto_mypage, name="goto_mypage"),
    path("mypage/"+"<str:name>", views.mypage, name="mypage"),
    path("edit_mypage/", views.edit_mypage, name="edit_mypage"),
    path("", RedirectView.as_view(url='/login/', permanent=True), name="login"),
]