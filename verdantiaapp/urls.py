from django.contrib import admin
from django.urls import path, include
from .views import home_view, login_view, logout_view, signup, check_auth

urlpatterns = [
    path('', home_view, name='home'),
    path("login/", login_view, name='login'),
    path("logout/", logout_view, name='logout'),
    path("signup/", signup, name='signup'),
    path("api/check-auth/", check_auth, name='check_auth'),
]