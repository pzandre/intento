from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView

from .forms import CustomPasswordForm, EditProfileForm, SignupForm

def password_success(request):
    return render(request, 'registration/password_success.html', {})


class PasswordsChangeView(PasswordChangeView):
    form_class = CustomPasswordForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password_success')


class UserRegisterView(generic.CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('dashboard')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        return self.request.user