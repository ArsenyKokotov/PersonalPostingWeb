#creating url paths

from django.urls import path

from . import views

urlpatterns = [
    path("", views.mypage, name="mypage"),
    path("mypage/", views.mypage, name="mypage"),
    path("edit_mypage/", views.edit_mypage, name="edit_mypage"),
]