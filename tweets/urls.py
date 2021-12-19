from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('delete/<int:id>', views.delete_post, name="delete_post"),
]
