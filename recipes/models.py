from django.db import models

# Create your models here.


class Recipe(models.Model):  # The recipe model that appears in the admin
    name = models.CharField(max_length=254)
    ingredients = models.TextField()
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
