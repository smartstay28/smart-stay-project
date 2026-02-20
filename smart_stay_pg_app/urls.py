from django.urls import path
from . import views

urlpatterns = [
    path("", views.select_role, name="select_role"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("welcome/", views.welcome, name="welcome"),
    path("logout/", views.logout_view, name="logout"),
]