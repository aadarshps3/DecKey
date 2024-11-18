from django.urls import path

from DecApp import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('loginpage', views.loginpage, name="loginpage"),
]
