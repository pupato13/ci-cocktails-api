from django.contrib import admin
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.urls import reverse
from django.utils.html import format_html, urlencode
from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    autocomplete_fields = ["featured_cocktail"]
    list_display = ["name", "cocktails_count"]
    search_fields = ["name"]

    @admin.display(ordering="cocktails_count")
    def cocktails_count(self, category):
        url = (
            reverse("admin:cocktails_cocktail_changelist")
            + "?"
            + urlencode({
                "category__id": str(category.id)
            }))
        return format_html("<a href='{}'>{} Cocktails</a>", url, category.cocktails_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            cocktails_count=Count("cocktails")
        )
    
@admin.register(models.Cocktail)
class CocktailAdmin(admin.ModelAdmin):
    autocomplete_fields = ["category"]
    list_display = ["name", "category_name"]
    list_filter = ["category"]
    list_per_page = 10
    list_select_related = ["category"]
    search_fields = ["name"]

    def category_name(self, product):
        return product.category.name