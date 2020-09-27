from django.urls import path
from .views import CarCreate, CarProfile, CarAll, CarEdit, CarDelete, CarRenting, CarRentingAdd

urlpatterns = [
    path('create/', CarCreate.as_view(), name='car_create_url'),
    path('profile/<int:pk>/', CarProfile.as_view(), name='car_profile_url'),
    path('all/', CarAll.as_view(), name='car_all_url'),
    path('edit/<int:pk>/', CarEdit.as_view(), name='car_edit_url'),
    path('delete/<int:pk>/', CarDelete.as_view(), name='car_delete_url'),

    path('renting/', CarRenting.as_view(), name='car_renting_url'),
    path('renting_add/', CarRentingAdd.as_view(), name='car_renting_add_url'),
]
