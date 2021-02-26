from django.shortcuts import render
from .models import Recipe


def view_recipes(request):
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }

    return render(request, 'recipes/recipes.html', context)
