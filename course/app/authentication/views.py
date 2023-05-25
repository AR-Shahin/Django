from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
# Create your views here.

from .forms import (
    LoginForm,RegisterForm
)

class LoginView(FormView):
    template_name = "auth/login.html"
    
    form_class = LoginForm
    success_url = reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = self.get_form()
        return context
    
    
class RegistrationView(FormView):
    template_name = "auth/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['register_form'] = self.get_form()
        return context

class LogoutView(TemplateView):
    pass


class DashboardView(TemplateView):
    template_name = "auth/dashboard.html"