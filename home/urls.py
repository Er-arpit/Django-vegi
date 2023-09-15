from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("services", views.services, name="services"),
    path("checkout", views.checkout, name="checkout"),
    path("registration", views.registration, name="registration"),
    path("login_page", views.login_page, name="login_page"),
    path("logout_page", views.logout_page, name="logout_page"),
]