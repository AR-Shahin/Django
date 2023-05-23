
from django.contrib import admin
from django.urls import path,include
from .views import *

app_name = "orm"

extra = [
    path("details", details),
    path("<str:name>",post),
]

urlpatterns = [
    path("",OneToOneView.as_view(),name="orm"),
    path("many-to-one",ManyToOneView.as_view(),name="m2o"),

    path("posts/",include(extra))
    # path("",ListView.as_view(),name="orm")
]


