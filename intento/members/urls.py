from django.urls import path
from .views import password_success, PasswordsChangeView, UserEditView, UserRegisterView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit-profile'),
    path('password/', PasswordsChangeView.as_view()),
    path('password_success', password_success, name='password_success'),
]
