from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.UserLogin, name='userlogin'),
    path('registration/', views.UserRegistration, name='userregistration'),
    path('password-reset/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/', views.MyPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
]