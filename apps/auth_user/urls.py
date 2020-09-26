from django.urls import path, include
from .views import RegistrationUser, LoginUser, LogOutUser
from renting_car.views import redirect_login
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', redirect_login),
    path('registration/', RegistrationUser.as_view(), name='registration_url'),
    path('login/', LoginUser.as_view(), name='login_url'),
    path('logout/', LogOutUser.as_view(), name='logout_url'),

    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='auth_user/password_reset/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='auth_user/password_reset/password_reset_sent.html'
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='auth_user/password_reset/password_reset_form.html'
    ), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='auth_user/password_reset/password_reset_done.html'
    ), name='password_reset_complete'),
]
