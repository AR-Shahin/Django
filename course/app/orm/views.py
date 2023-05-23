from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import (
    Place,Waiter,Restaurant,Category,Post
)
import random
 
# Create your views here.


class OneToOneView(TemplateView):
    
    
    def post(self, request, *args, **kwargs):
        
        if request.POST['flag'] == 'place':
            if request.POST['place']:
                p = Place(name= request.POST['place'],address='ABC')
                p.save()
        
        elif request.POST['flag'] == 'restaurant':
            if request.POST['place']:
                r = Restaurant(
                    place= Place.objects.filter(pk=request.POST['place'])[0],
                    serves_hot_dogs = random.randint(1, 10) % 2 == 0 if True else False, 
                    serves_pizza = random.randint(1, 10) % 2 == 0 if True else False, 
                    )
                r.save()
                
            
        elif request.POST['flag'] == 'waiter':
            if request.POST['restaurant']:
                w = Waiter(
                    restaurant= Restaurant.objects.filter(pk=request.POST['restaurant'])[0],
                    name = request.POST['name']
                    )
                w.save()
        
        return self.get(request, *args, **kwargs)
    
    
    def get_context_data(self, **kwargs: Any):
        
        context = super().get_context_data(**kwargs)

        context["places"] = Place.objects.all()
        context["restaurants"] = Restaurant.objects.all()
        context["waiters"] = Waiter.objects.all()
        
         
        return context
    
    template_name = "orm/index.html"


class ManyToOneView(TemplateView):
    
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        
        context['categories'] = Category.objects.prefetch_related("posts").all()
        context['posts'] = Post.objects.all()
        
        return context
    
    template_name = "orm/m2o.html"
    
    
    
def post(request,name):
    return HttpResponse(fun(name,"jjj"))
    
def fun(*args):return [arg for arg in args]

def details(req): return HttpResponse("Hello")