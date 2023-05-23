from django.shortcuts import render
from django.views.generic import TemplateView
from .models import (Category)
from .seeders import *
class HomeView(TemplateView):
  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    
    
    template_name = "ecom/index.html"