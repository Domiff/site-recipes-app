from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from .forms import CreateUserForm


class RegisterUserView(CreateView):
    model = User
    form_class = CreateUserForm
    template_name = "auth/registration.html"
    success_url = reverse_lazy("auth_user:login")


class LoginUserView(LoginView):
    template_name = "auth/log_in.html"
    success_url = reverse_lazy("site_recipes:main")


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    _url = reverse("auth_user:login")
    return redirect(_url)
