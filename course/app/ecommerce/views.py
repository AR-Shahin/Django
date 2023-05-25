from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import (Category)
from .seeders import *


def seeder(request):
    # color_seeder()
    # size_seeder()
    
    return redirect('/')
class HomeView(TemplateView):
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    
    
    template_name = "ecom/index.html"
    
    
class ShopView(TemplateView):   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["numbers"] = [i for i in range(0,6)]
        return context
    
    
    template_name = "ecom/pages/shop.html"
    
    
class CartView(TemplateView):   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["numbers"] = [i for i in range(0,6)]
        return context


    template_name = "ecom/pages/cart.html" 
    
    