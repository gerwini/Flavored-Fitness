from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_recipes, name='recipes'),
    path('<int:recipe_id>', views.recipe_info, name='recipe_info'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('edit/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('delete/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
]
