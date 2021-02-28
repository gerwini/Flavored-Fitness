from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Recipe(models.Model):  # The recipe model that appears in the admin
    name = models.CharField(max_length=254)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    ingredients = ArrayField(
        models.TextField(max_length=99, blank=True),
        size=20, default=list
    )
    preparation_steps = ArrayField(
        models.TextField(max_length=99, blank=True),
        size=20, default=list
    )


    def __str__(self):
        return self.name
