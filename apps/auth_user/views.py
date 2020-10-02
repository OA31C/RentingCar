from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .forms import LoginForm, RegisterForm
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from .models import User


class RegistrationUser(CreateView):
    form_class = RegisterForm
    template_name = 'auth_user/registration.html'
    success_url = reverse_lazy('login_url')


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'auth_user/login.html'

    """Override method to go to the login"""

    def get_success_url(self):
        auth_user = self.request.user
        messages.add_message(
            self.request, messages.SUCCESS, _('Welcome to site! ') + auth_user.username)
        return reverse('user_profile_url', kwargs={'pk': auth_user.pk})


class LogOutUser(LogoutView):
    next_page = reverse_lazy('login_url')


class UserProfile(LoginRequiredMixin, View):
    login_url = 'login_url'

    def get(self, request, pk):
        user = User.objects.get(id=pk)
        return render(request, 'auth_user/user_profile.html', context={'user': user})


class UserEdit(LoginRequiredMixin, UpdateView):
    login_url = 'login_url'
    model = User
    fields = ['username', 'email', 'language']
    template_name = 'auth_user/user_edit.html'

    """Override method to go to the user profile"""

    def get_success_url(self):
        object_user = self.request.user
        messages.add_message(
            self.request, messages.SUCCESS, self.request.user.username + _(' is success edit!'))
        return reverse('user_profile_url', kwargs={'pk': object_user.pk})

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        if self.request.user.email != kwargs['instance'].email:
            return self.handle_no_permission()
        return kwargs


class UserDelete(LoginRequiredMixin, View):
    login_url = 'login_url'

    def get(self, request, pk):
        user = User.objects.get(id=pk)
        return render(request, 'auth_user/user_delete.html', context={'user': user})

    def post(self, request, pk):
        user = User.objects.get(id=pk)
        logged_in_user = self.request.user
        if logged_in_user.email != user.email:
            return HttpResponse('<h1>This user has no rights to this action</h1>')
        user.delete()
        return redirect('login_url')
