
from django.contrib import admin
from django.urls import path,include
from .views import *

app_name = "ecom"


urlpatterns = [
    path("",HomeView.as_view(),name="home"),
    path("seeder",seeder,name="seeder"),
    path("shop",ShopView.as_view(),name="shop"),
    path("cart",CartView.as_view(),name="cart")
  
]


