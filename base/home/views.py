from django.shortcuts import render, redirect
from . forms import UserPersonalDataForm, UserMedicalDataForm, UserDeitDataForm
from accounts.models import CustomUser
from django.contrib import messages
from django.urls import reverse
from . models import UserPersonalData, UserMedicalData, UserDietryData

# Create your views here.

def Dashboard(request):
    return render(request, 'home/index.html')


def UserPersonalDetails(request, pk):
    if request.method == 'POST':
        user = request.user
        isPresent = UserPersonalData.objects.filter(user = user).first()
        if isPresent:
            messages.info(request, 'Personal data already present.')
            return redirect(reverse('usermedicaldetails', args=[pk]))
        else:
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
                return redirect(reverse('usermedicaldetails', args=[pk]))
            else:
                messages.error(request, 'Oh. Snap something just broke. Try again.')
    return render(request, 'home/personaldata/userpersonaldata.html')


def EditUserPersonalData(request, pk):
    personaldata = UserPersonalData.objects.get(id=pk)
    if request.method == 'POST':
        form = UserPersonalDataForm(request.POST, instance=personaldata)
        if form.is_valid():
            form.save()
            messages.success(request, 'Personal data updated successfully.')
    context = {
        'data':personaldata
    }
    return render(request, 'home/personaldata/editpersonaldata.html', context)


def UserMedicalDetails(request, pk):
    if request.method == 'POST':
        user = request.user
        isPresent = UserMedicalData.objects.filter(user = user).first()
        if isPresent:
            messages.info(request, 'Personal data already present.')
            return redirect(reverse('userdietdetails', args=[pk]))
        else:
            form = UserMedicalDataForm(request.POST, request.FILES)
            if form.is_valid():  
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
                messages.success(request, 'Medical details saved...')
                return redirect(reverse('userdietdetails', args=[pk]))
            else:
                print(form.errors)
                messages.error(request, 'Oh. Snap something just broke. Try again.')
    return render(request, 'home/medicaldata/usermedicaldata.html')



def UserDietDetails(request, pk):
    if request.method == 'POST':
        user = request.user
        isPresent = UserDietryData.objects.filter(user = user).first()
        
        if isPresent:
            data = UserDietryData.objects.get(user = user)
            messages.info(request, 'Dietery data already present.')
            return redirect(reverse('confirmpage', args=[pk, data.id]))
        else:
            form = UserDeitDataForm(request.POST)
            if form.is_valid():  
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
                messages.success(request, 'Diet details saved...')
                return redirect(reverse('confirmpage', args=[pk, obj.id]))
            else:
                print(form.errors)
                messages.error(request, 'Oh. Snap something just broke. Try again.')
    return render(request, 'home/dietdata/userdietdata.html')



def ConfirmPage(request, user, diet):
    if request.method=='POST':
        return redirect('bufferpage')
    return render(request, 'home/confirmpage.html')


def Buffer(request):
    return render(request, 'home/bufferpage.html')