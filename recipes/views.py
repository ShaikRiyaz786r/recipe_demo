from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def recipe(request):
    if request.method=="POST":
        recipename = request.POST.get('recipename')
        recipedesc = request.POST.get('recipedesc')
        recipeimg = request.FILES.get('image')
        data = Recipe.objects.create(recipe_name=recipename,recipe_desc=recipedesc,recipe_img=recipeimg)
        data.save()
    return render(request,'recipes.html')
