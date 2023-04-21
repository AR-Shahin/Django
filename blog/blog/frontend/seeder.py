from .models import *
from helpers.helper import *
def create_category():
    categories = ["Sports","Politics","Science","Technology"]
    
    for category in categories:
        Category.objects.create(
            name = category
        )
    
def create_sub_category():
    categories = ["Sports 1","Politics 2","Science 1","Technology 1"]
    
    for category in categories:
        SubCategory.objects.create(
            name = category,
            category_id = Category.objects.get(pk=rand_int(1,4))
        )