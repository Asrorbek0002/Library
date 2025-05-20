from django.urls import path
from django.contrib import admin
from books.views import HelloWorldView



urlpatterns = [
    path('hello/',HelloWorldView.as_view(), name = "hello_html" ),
]


