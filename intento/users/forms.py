from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import Group
from .models import CustomUser
from institutes.models import Institute


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    institute = forms.ModelChoiceField(queryset=Institute.objects.all(),
                                       required=True, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'is_staff', 'is_active', 'group', 'institute')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        # self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'is_staff', 'is_active', 'group', 'institute')


class CustomPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, label="Senha anterior",
                                   widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=100, label="Nova senha",
                                    widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=150, label="Repita a nova senha",
                                    widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = CustomUser
        fields = ('old_password', 'new_password1', 'new_password2')


class EditUserForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    institute = forms.ModelChoiceField(queryset=Institute.objects.all(),
                                       required=True, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'password', 'is_staff', 'is_active', 'group', 'institute')

