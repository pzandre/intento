from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomPasswordForm, EditUserForm


def logout_successful(request):
    return render(request, 'registration/logout.html', {})


def password_success(request):
    return render(request, 'registration/password_success.html', {})


class PasswordsChangeView(PasswordChangeView):
    form_class = CustomPasswordForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password_success')


class UserCreation(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')


class UserEdit(UpdateView):
    form_class = EditUserForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        return self.request.user
