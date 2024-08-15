from django.forms import ModelForm
from . models import UserPersonalData, UserMedicalData


class UserPersonalDataForm(ModelForm):
    class Meta:
        model = UserPersonalData
        exclude = ('time_stamp', 'id', 'user', 'first_name', 'last_name')


class UserMedicalDataForm(ModelForm):
    class Meta:
        model = UserMedicalData
        exclude = ('time_stamp', 'last_updated', 'id', 'user')