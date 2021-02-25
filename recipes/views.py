from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages


def view_recipes(request):
    return render(request, 'recipes/recipes.html')
