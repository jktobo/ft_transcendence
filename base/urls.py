from django.urls import path, include
from .views import authView, home

from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", home, name="home"),
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("login/", LoginView.as_view(), name="login"),  # Кастомный URL для входа
]
