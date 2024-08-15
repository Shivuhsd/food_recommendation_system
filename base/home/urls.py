from django.urls import path
from . import views



urlpatterns = [
    path('', views.Dashboard, name='dashboard'),
    path('details/confirm/<uuid:user>/<uuid:diet>/', views.ConfirmPage, name='confirmpage'),
    path('bufferpage/', views.Buffer, name='bufferpage'),

    # PersonalDetailsCRUD
    path('userpersonaldetails/<uuid:pk>/', views.UserPersonalDetails, name='userpersonaldetails'),
    path('<str:pk>/edituserpersonaldata/', views.EditUserPersonalData, name='edituserpersonaldata'),


    #MedicalDetailsCRUD
    path('usermedicaldetails/<uuid:pk>/', views.UserMedicalDetails, name='usermedicaldetails'),


    #DietDetailsCRUD
    path('userdietdetails/<uuid:pk>/', views.UserDietDetails, name='userdietdetails'),
]