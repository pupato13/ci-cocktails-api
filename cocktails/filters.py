from django_filters.rest_framework import FilterSet
from .models import Cocktail

class CocktailFilter(FilterSet):
  class Meta:
    model = Cocktail
    fields = {
      "category_id": ["exact"],
    }