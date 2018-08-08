from django.urls import path
from . import views

from django.conf import settings

from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    #path('', views.user_login, name="user_login"),
    path('login', views.user_login, name="user_login"),
    # path('new-login', auth_views.login, {'template_name': 'account/login.html'}, name="user_login"),
    path('logout', auth_views.logout, {'template_name': 'accounts/logout.html'}, name='user_logout'),
    path('register/', views.user_register, name='user_register'),#斜线被坑了很久

]
