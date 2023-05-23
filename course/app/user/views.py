from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.urls import reverse_lazy

from .forms import (UserCreateForm)

from .models import (User)

class TestView(TemplateView):
    flag = "ars"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["flag"] = self.flag
        context["template"] = self.get_template_names()
        
        return context
    
    template_name = "user/index.html"
    
    
class ArsView(TestView):
    flag = "Boom"
    pass


class UserListView(ListView):
    model = User
    context_object_name = "users"
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ars"] = "AR Shahin"
        return context
    
    template_name='user/index.html'
    
    
    
class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name='user/create.html'
    success_url = reverse_lazy("users")
    





  