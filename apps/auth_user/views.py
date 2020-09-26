from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from .forms import LoginForm, RegisterForm


class RegistrationUser(generic.CreateView):
    form_class = RegisterForm
    template_name = 'auth_user/registration.html'
    success_url = reverse_lazy('login_url')


class LoginUser(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'auth_user/login.html'

    """Override method to the url"""
    def get_success_url(self):
        return reverse_lazy('login_url')


class LogOutUser(auth_views.LogoutView):
    next_page = reverse_lazy('login_url')

