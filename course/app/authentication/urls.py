
from django.contrib import admin
from django.urls import path,include
from .views import *

app_name = "auth"


urlpatterns = [
    path("login",LoginView.as_view(),name="login"),
    path("register",RegistrationView.as_view(),name="register"),
    path("logout",LogoutView.as_view(),name="logout"),
    path("dashboard",DashboardView.as_view(),name="dashboard"),

]


