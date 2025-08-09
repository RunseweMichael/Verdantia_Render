from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import login, logout
from django.http import JsonResponse

def get_frontend_url(request):
    origin = request.META.get("HTTP_ORIGIN")
    if origin in settings.FRONTEND_URLS:
        return origin
    return settings.FRONTEND_URLS[1]  # Default to production if unknown

def home_view(request):
    return render(request, 'home.html')

@login_required
def check_auth(request):
    return JsonResponse({'authenticated': True, 'username': request.user.username})

def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(get_frontend_url(request))
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect(f"{get_frontend_url(request)}/login")

def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})
