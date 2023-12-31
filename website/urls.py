from django.urls import path
from .views import *

urlpatterns = [
    path("", login, name="login"),
    path("header",header, name="header"),
    path("home",home,name="home"),
    path("about", about, name="about"),
    path("contact", contact, name="contact"),
    path("feedback", feedback, name="feedback"),
    path("register", register, name="register"),
    path("menu", menu, name="menu"),
    path("logout", logout, name="logout"),
    path("login", login, name="login"),
    path("modifymenu", modifymenu, name="modifymenu"),
    path("buy", buy, name="buy"),
]