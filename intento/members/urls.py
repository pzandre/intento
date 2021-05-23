from django.urls import path
from .views import password_success, PasswordsChangeView, UserEditView, UserRegisterView, InstituteListView,\
                   InstituteCreateView, InstituteDetailView, ProfileDetailView, ProfileUpdateView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit-profile'),
    path('password/', PasswordsChangeView.as_view()),
    path('password_success/', password_success, name='password_success'),
    path('institutes/', InstituteListView.as_view(), name='institutes'),
    path('institute/create/', InstituteCreateView.as_view(), name='new-institute'),
    path('institute/<int:pk>/', InstituteDetailView.as_view(), name='institute-details'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-details'),
    path('profile/create/<int:pk>', ProfileUpdateView.as_view(), name='new-profile'),
]
