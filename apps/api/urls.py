from django.urls import path, include
from .views import UserCreateViewAPI, UserListViewAPI, UserDetailViewAPI


urlpatterns = [
    path('users_all/', UserListViewAPI.as_view(), name='api_users_all_url'),
    path('user/create/', UserCreateViewAPI.as_view(), name='api_user_create_url'),
    path('user/detail/<int:pk>/', UserDetailViewAPI.as_view(), name='api_user_detail_url'),
]
