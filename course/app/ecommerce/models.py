from django.db import models
from django.db.models import CharField


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ecom_categories'
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    """
    Fashion & Beauty
    Kids & Babies 
    Men & Women 
    Gadgets & Accessories
    Electronics & Accessories
    """


class Size(models.Model):
    name = models.CharField(max_length=120)
    slug = models.CharField(max_length=120)
    
    def __str__(self) -> CharField:
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=120)
    slug = models.CharField(max_length=120)
    
    def __str__(self) -> CharField:
        return self.name

class Product(models.Model):
    category = models.OneToOneField(
        Category,
        on_delete=models.CASCADE
    )
    color = models.OneToOneField(
        Color,
        on_delete=models.CASCADE
    )
    size = models.OneToOneField(
        Size,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=120)
    slug = models.CharField(max_length=120)
    price = models.FloatField(default=120)
    quantity = models.IntegerField(default=10)
    image = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self) -> CharField:
        return self.name
