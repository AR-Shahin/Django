from .models import *



colors = ["Red","Green","Blue","Pink","Yellow"]
sizes = ["S","L","XL","XXL"]


def color_seeder():  
    for color in colors:
        c = Color(name = color, slug = color)
        c.save()


def size_seeder():  
    for size in sizes:
        s = Size(name = size, slug = size)
        s.save()