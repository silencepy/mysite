from django.urls import path
from . import views

from django.conf import settings

from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.user_login, name="user_login"),
    # path('new-login', auth_views.login, {'template_name': 'account/login.html'}, name="user_login"),
    path('logout/', auth_views.logout, {'template_name': 'accounts/logout.html'}, name='user_logout'),
    path('register/', views.user_register, name='user_register'),  # 斜线被坑了很久
    path('password-change/', auth_views.password_change, {"post_change_redirect": "/accounts/password-change-done",
                                                          'template_name': 'accounts/password_change_form.html'},
         name='password_change'),
    path('password-change-done/', auth_views.password_change_done,
         {'template_name': 'accounts/password_change_done.html'}, name='password_change_done'),
    path('password-reset/', auth_views.password_reset, {"template_name": "accounts/password_reset_form.html",
                                                        "email_template_name": "accounts/password_reset_email.html",
                                                        "subject_template_name": "accounts/password_reset_subject.txt",
                                                        "post_reset_redirect": "/accounts/password-reset-done"},
         name="pasword_reset"),
    path('password-reset-done/', auth_views.password_reset_done, {"template_name": "accounts/password_reset_done.html"},
         name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.password_reset_confirm,
         {"template_name": "accounts/password_reset_confirm.html",
          "post_reset_redirect": "/accounts/password-reset-complete"}, name="password_reset_confirm"),
    path('password-reset-complete/', auth_views.password_reset_complete,
         {"template_name": "accounts/password_reset_complete.html"}, name="password_reset_complete"),
    path("my-information/", views.myself, name="my_information"),
    path("edit-my-information/", views.myself_edit, name="edit_my_information"),

]
