from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required


def view_recipes(request):  # Main Recipes page listing the recipes that are stored as models
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }

    return render(request, 'recipes/recipes.html', context)


def recipe_info(request, recipe_id):  # Lists the information of the recipe when clicked on

    recipes = get_object_or_404(Recipe, pk=recipe_id)

    context = {
        'recipe': recipes,
    }

    return render(request, 'recipes/recipe_info.html', context)


@login_required
def add_recipe(request):  # Lets the admins and superusers create new recipes
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            messages.success(request, 'Successfully added recipe!')
            return redirect(reverse('recipe_info', args=[recipe.id]))
        else:
            messages.error(request, 'Failed to add recipe. Please ensure the form is valid.')
    else:
        form = RecipeForm()

    template = 'recipes/add_recipe.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_recipe(request, recipe_id):  # Lets admins edit recipes
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated recipe!')
            return redirect(reverse('recipe_info', args=[recipe.id]))
        else:
            messages.error(request, 'Failed to update recipe. Please ensure the form is valid.')
    else:
        form = RecipeForm(instance=recipe)
        messages.info(request, f'You are editing {recipe.name}')

    template = 'recipes/edit_recipe.html'
    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(request, template, context)


@login_required
def delete_recipe(request, recipe_id):  # Lets admins delete recipes in the list
    """ Delete a recipe from the Recipe List """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()
    messages.success(request, 'recipe deleted!')
    return redirect(reverse('recipes'))
