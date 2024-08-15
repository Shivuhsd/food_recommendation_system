from django.db import models
import uuid
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class UserPersonalData(models.Model):
    id = models.UUIDField(primary_key=True, editable = False, default = uuid.uuid4)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='profile_img/')
    phone_number = models.CharField(max_length=100, blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    dob = models.DateField(blank=False, null=False)
    age = models.CharField(max_length=3, null=False, blank=False)
    weight = models.DecimalField(max_digits = 3, decimal_places = 2)
    height = models.CharField(max_length = 4, null=True, blank = True)
    health_history = models.TextField(null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.user.first_name
    
    
# Model to store Health Data
    
def user_medical_data_upload_to(instance, filename):
    # Generate a unique file name and path for each file
    return f'reports/{instance.id}/{filename}'

class UserMedicalData(models.Model):
    id = models.UUIDField(primary_key=True, editable = False, default = uuid.uuid4)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hemoglobin_level = models.DecimalField(max_digits = 3, decimal_places = 2)
    blood_type = models.CharField(max_length=10, null=False, blank=True)
    vitamin_b12 = models.CharField(max_length=20, null=True, blank=False)
    iron_levels = models.DecimalField(max_digits = 3, decimal_places = 2)
    rbc_count = models.CharField(max_length=10, null=True, blank = False)
    medication = models.TextField(null=True, blank = True)
    reports = models.FileField(upload_to=user_medical_data_upload_to)
    time_stamp = models.DateTimeField(auto_now_add = True)
    last_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"Medical Data for {self.user.first_name}"
    

# User Dietery Information
    
class UserDietryData(models.Model):
    id = models.UUIDField(primary_key=True, editable = False, default = uuid.uuid4)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    




