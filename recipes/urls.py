from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_recipes, name='recipes'),
]