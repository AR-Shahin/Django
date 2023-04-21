from django.db import models



# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    
    def display(self):
        return f"Name {self.name}"
    
class SubCategory(models.Model):
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


