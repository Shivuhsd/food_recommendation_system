from django.contrib import admin
from . models import UserPersonalData, UserMedicalData

# Register your models here.
admin.site.register(UserMedicalData)
admin.site.register(UserPersonalData)
