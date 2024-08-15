from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard, name='dashboard'),
    path('userpersonaldetails/<str:pk>/', views.UserPersonalDetails, name='userpersonaldetails'),
    path('usermedicaldetails/<str:pk>/', views.UserMedicalDetails, name='usermedicaldetails'),
]