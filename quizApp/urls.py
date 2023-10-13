from django.contrib import admin
from django.urls import path, include
from .views import home, questionEditList, editQuestion

urlpatterns = [
    path("", home, name="home"),
    path("questionEditList", questionEditList, name="questionEditList"),
    path("editQuestion", editQuestion, name="editQuestion"),
]
