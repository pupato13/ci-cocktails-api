from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    featured_cocktail = models.ForeignKey(
        "Cocktail", on_delete=models.SET_NULL, null=True, related_name="+", blank=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"

class Cocktail(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=255)
    directions = models.CharField(max_length=400)
    photo_url = models.CharField(max_length=400)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="cocktails")
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ["name"]