from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from .forms import CustomRegistrationForm, LoginForm
from events.models import Event, Category
from django.utils import timezone
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    form = CustomRegistrationForm()
    
    if request.method == "POST":
        form = CustomRegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.is_active = False
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect("sign_in")
    
    context = {
        "form": form
    }
    return render(request, "register.html", context)

def sign_in(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect("home")
    context = {
        "form": form
    }
    return render(request, "login.html", context)

@login_required
def sign_out(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "Logged out successfully!")
        return redirect("home")
    return redirect("home")

def activate_user(request, user_id, token):
    try:
        user = User.objects.get(id=user_id)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('sign_in')
        else:
            return HttpResponse('Invalid Id or token')

    except User.DoesNotExist:
        return HttpResponse('User not found')