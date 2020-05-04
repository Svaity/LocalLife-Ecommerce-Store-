from django.urls import path
from .views import register, profile, change_password
from django.contrib.auth import views as auth_views
from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required

from django.conf.urls import url

from .views import my_orders

app_name = 'accounts'

urlpatterns = [
    path('order/', my_orders),
    #     url('order', my_orders, name='my_profile'),
    path('user/register/',
         unauthenticated_user(register),
         name='register'),
    path('user/profile/',
         profile,
         name='profile'),
    path('user/password-change/',
         change_password,
         name='password_change'),
    path('user/login/',
         auth_views.LoginView.as_view(template_name='user/login.html'),
         name='login'),
    path('user/logout/',
         login_required(auth_views.LogoutView.as_view(
             template_name='user/logout.html')),
         name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='user/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='user/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='user/password_reset_confirm.html'),
         name='password_reset_confirm'),
    #     url(r'order', my_orders, name='my_order')
]
