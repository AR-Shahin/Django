from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .seeder import *
from helpers.helper import *
# Create your views here.

def index(request):
    
    # cat = Category.objects.create(name="ars",description="dddddd")
    data = {
        "content" : "The tale begins in Mumbai where a sophisticated gang of robbers is sweeping through the city, giving nightmares to the police department. They come like wind, sweep the place and disappear on their hi-tech bikes - the slickest and fastest riding machines on the road.",
        "categories" : Category.objects.all(),
        "sub_categories" : SubCategory.objects.all()
    }
    return render(request,"frontend/index.html",data)


def about(request):
    return render(request,"frontend/about.html")

def user(request,name):
    data = {
        "name" : name
    }
    return render(request,"frontend/user.html",data)