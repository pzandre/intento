from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import PasswordChangeView
from .models import Institute, Profile
from .forms import CustomPasswordForm, EditProfileForm, SignupForm, CreateInstituteForm, CreateProfileForm


def password_success(request):
    return render(request, 'registration/password_success.html', {})


class PasswordsChangeView(PasswordChangeView):
    form_class = CustomPasswordForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password_success')


class UserRegisterView(CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'
    # success_url = reverse_lazy('new-profile', kwargs={'pk': super().object.pk})
    def get_success_url(self):
        view_name = 'new-profile'
        return reverse(view_name, kwargs={'pk': self.object.pk})


class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        return self.request.user


class InstituteCreateView(CreateView):
    form_class = CreateInstituteForm
    template_name = 'create_institute.html'
    success_url = reverse_lazy('institutes')


class InstituteListView(ListView):
    model = Institute
    template_name = 'institutes.html'


class InstituteDetailView(DetailView):
    model = Institute
    template_name = 'institute_details.html'


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile_details.html'


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'new_profile.html'
    success_url = reverse_lazy('profile-details')
