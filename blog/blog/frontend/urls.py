
from django.urls import path

from .views import *
from .models import *
urlpatterns = [
    path("", index, name="home"),
    path("about", about, name="about"),
    path("user/<name>", user, name="user"),

]
