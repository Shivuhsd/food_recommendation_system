from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from . forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from . models import CustomUser

# Create your views here.


def UserLogin(request):
    if request.user.is_authenticated:
        pass
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username = username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, 'Succesfully loged in.')
            else:
                messages.error(request, 'Something went wrong while logging')
    return render(request, 'accounts/userlogin.html')



def UserRegistration(request):
    if request.user.is_authenticated:
        pass
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid() and form.match_password:
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
           
            try:
                user = CustomUser.objects.create_user(email, email, password)
                user.save()
                messages.success(request, 'User Successfully Registered.')
                user = authenticate(request, username=email, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login succesfull.')
                    return redirect(reverse('userpersonaldetails', args=[user.id]))
                else:
                    messages.error(request, 'Login failed. Try again..')
                    return redirect('userlogin')
            except Exception as e:
                messages.error(request, f'{e}Provided email already registered with us, use another email.')
        else:
            messages.error(request, 'Check email and password you provided.')
    return render(request, 'accounts/userregister.html')


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/reset_password_email.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/msg.txt'
    success_message = "We've emailed you instructions for setting your password..."
    success_url = reverse_lazy('userlogin')



class MyPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    template_name = 'accounts/confirm_password.html'
    success_message = "Your password has been successfully updated..."
    success_url = reverse_lazy('userlogin')




