from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from .forms import CustomRegistrationForm, LoginForm
from events.models import Event, Category
from django.utils import timezone
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, View
from django.contrib.auth.views import LoginView, LoginView, LogoutView
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.

# def register(request):
#     form = CustomRegistrationForm()
    
#     if request.method == "POST":
#         form = CustomRegistrationForm(request.POST)
        
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data["password1"])
#             user.is_active = False
#             user.save()
#             messages.success(request, "Account created successfully!")
#             return redirect("sign_in")
    
#     context = {
#         "form": form
#     }
#     return render(request, "register.html", context)

class RegisterView(UserPassesTestMixin, CreateView):
    model = User
    form_class = CustomRegistrationForm
    template_name = "register.html"
    success_url = reverse_lazy("sign_in")
    
    def test_func(self):
        return not self.request.user.is_authenticated

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password1"])
        user.is_active = False
        user.save()
        messages.success(self.request, "Account created successfully!")
        return super().form_valid(form)

# def sign_in(request):
#     form = LoginForm()
#     if request.method == "POST":
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             messages.success(request, "Logged in successfully!")
#             return redirect("home")
#     context = {
#         "form": form
#     }
#     return render(request, "login.html", context)

class SignInView(UserPassesTestMixin, LoginView):
    form_class = LoginForm
    template_name = "login.html"
    # success_url = reverse_lazy("home") ## LoginView already has a default success url which is settings.LOGIN_REDIRECT_URL, so we can set that in settings.py instead of here.

    def test_func(self):
        return not self.request.user.is_authenticated
    
    def get_success_url(self):
        return reverse_lazy("home")
    
# @login_required
# def sign_out(request):
#     if request.method == "POST":
#         logout(request)
#         messages.success(request, "Logged out successfully!")
#         return redirect("home")
#     return redirect("home")

# class SignOutView(View):
#     def post(self, request):
#         logout(request)
#         messages.success(request, "Logged out successfully!")
#         return redirect("home")
    
class SignOutView(LogoutView):
    next_page = reverse_lazy("home")

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