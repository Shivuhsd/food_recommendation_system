from django.shortcuts import render, redirect
from . forms import UserPersonalDataForm, UserMedicalDataForm
from accounts.models import CustomUser
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def Dashboard(request):
    return render(request, 'home/index.html')


def UserPersonalDetails(request, pk):
    if request.method == 'POST':
        form = UserPersonalDataForm(request.POST, request.FILES)
        if form.is_valid():
            firstname = request.POST['first_name']
            lastname = request.POST['last_name']
            
            user = CustomUser.objects.get(id=pk)
            user.first_name = firstname
            user.last_name = lastname
            user.save()

            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, 'Personal details saved...')
            return redirect(reverse('usermedicaldetails', args=['pk']))
        else:
            messages.error(request, 'Oh. Snap something just broke. Try again.')
    return render(request, 'home/userpersonaldata.html')


def UserMedicalDetails(request, pk):
    return render(request, 'home/usermedicaldata.html')
