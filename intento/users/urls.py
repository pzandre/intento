from django.urls import path
from .views import UserCreation, UserEdit, logout_successful, PasswordsChangeView, password_success
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('new-user/', UserCreation.as_view(), name='user-creation'),
    path('edit-user/', UserEdit.as_view(), name='edit-user'),
    path('login/', LoginView.as_view(), {
        'template_name': 'registration/login.html'}),
    path('logout-successful/', logout_successful, name='logout-successful'),
    path('password/', PasswordsChangeView.as_view(), name='password-change'),
    path('password/successfully-changed/', password_success, name='password_success'),
]
