
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/",LoginView.as_view(template_name="Users/login.html"), name="login"),
    path("logout/",views.logout_view, name="logout"),
]