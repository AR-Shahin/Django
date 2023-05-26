from typing import Any
from django.http import HttpRequest, HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import (
    LoginForm,RegisterForm
)

from .models import (
    User
)

class LoginView(FormView):
    template_name = "auth/login.html"
    
    form_class = LoginForm
    success_url = reverse_lazy('auth:dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = self.get_form()
        return context
    

    def form_valid(self, form):
        
        if False:
            messages.warning(self.request,"Something went Wrong!")
            return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
        
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request,username=username,password=password)

        if user is None:
            messages.warning(self.request,"Wrong Credentials")
            return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
        
        login(self.request,user)
        return super().form_valid(form)
        

    

    
class RegistrationView(FormView):
    template_name = "auth/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('auth:login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['register_form'] = self.get_form()
        return context
    
    def form_valid(self, form):  
        if False:
            messages.warning(self.request,"Something went Wrong!")
            return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
        
        userName = form.cleaned_data["username"]
        email = form.cleaned_data["email"]
        # password = make_password(form.cleaned_data["password"])
        password = form.cleaned_data["password"]
        
        user = User(username = userName, email= email,password=password)
        
        user.save()
        messages.success(self.request,"Registration Successfully Done!!")

        return super().form_valid(form)

class LogoutView(View):

    def post(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect("login")
    


class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = "auth/dashboard.html"
    login_url = "/auth/login"