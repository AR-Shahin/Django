from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=120,unique=True)
    email = models.EmailField(max_length=120,unique=True)
    password = models.CharField(max_length=120)
    status = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'auth_users'
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'User'