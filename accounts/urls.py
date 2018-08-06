from django.urls import path
from . import views

from django.conf import settings

from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('', views.user_login, name="user_login"),
    # path('', auth_views.login, name="user_login"),
    path('login', views.user_login, name="user_login"),
    # path('login', auth_views.login, name="user_login"),
    path('logout', auth_views.logout, {"template_name": "accounts/logout.html"}, name='user_logout'),
]
