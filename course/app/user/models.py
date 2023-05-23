from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _






class User(models.Model):
    name = models.CharField(db_column="name",max_length=100,verbose_name= _("Name"))
    
    
    def demo(self):
        if self.name == "shahin":
            return 1
        else: return 2
    
    @property
    def get_name_with_designation(self):
        
        return f"Mr. {self.name}"
    
    def __str__(self) -> str:
        return self.name




    

