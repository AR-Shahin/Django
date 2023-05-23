from django import forms
from .models import (
    User
)
class UserCreateForm(forms.Form):
    
    class Meta():
        model = User
        fields = ['name']