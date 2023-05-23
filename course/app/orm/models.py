from typing import Any
from django.db import models

# Create your models here.
# class Rank(models.Model):
#     name = models.CharField(max_length=128)
    
#     def __str__(self):
#         return self.name
    
# class Person(models.Model):
#     name = models.CharField(max_length=128)
#     email = models.EmailField(max_length=128,null=True)
#     rank = models.OneToOneField(Rank,on_delete=models.CASCADE)
#     def __str__(self):
#         return self.name
    

# class Info(models.Model):
    # person = models.OneToOneField(Person,on_delete=models.CASCADE)
    # city = models.CharField(max_length=10)
    # zip = models.IntegerField()
    # phone = models.CharField(max_length=15)
    
    
    # def __str__(self):
    #     return self.person.name
    
    

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place" % self.name
    
    class Meta:
        ordering = ["-id"]

class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)
    
    


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name
        
    class Meta:
        db_table = 'categories'
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ["-id"]
    
    
class Post(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='posts')
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name