
from django.contrib import admin
from django.urls import path
from .views import *

app_name = "user"

urlpatterns = [
    path("", UserListView.as_view(),name="users"),
    path("create", UserCreateView.as_view(),name="create"),
    path("test", ArsView.as_view(),name="test"),
]
