from django.shortcuts import render, get_object_or_404
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required


def view_recipes(request):
    recipes = Recipe.objects.all()
    print(recipes)

    context = {
        'recipes': recipes,
    }

    return render(request, 'recipes/recipes.html', context)


def recipe_info(request, recipe_id):

    recipes = get_object_or_404(recipe, pk=recipe_id)

    context = {
        'recipe': recipes,
    }

    return render(request, 'recipes/recipe_info.html', context)


@login_required
def add_recipe(request):
    """ Add a recipe to the store """
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
