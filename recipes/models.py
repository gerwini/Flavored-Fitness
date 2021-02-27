from django.db import models

# Create your models here.


class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Recipe(models.Model):
    name = models.CharField(max_length=254)
    ingredients = models.TextField()
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.name
