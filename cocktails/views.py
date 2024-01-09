from django.db.models.aggregates import Count
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .filters import CocktailFilter
from .models import Category, Cocktail
from .pagination import DefaultPagination
from .serializers import CategorySerializer, CocktailSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(
        cocktails_count=Count("cocktails")).all()
    serializer_class = CategorySerializer

    def delete(self, request, id):
        category = get_object_or_404(Category, pk=id)
        if category.cocktails.count() > 0:
            return Response({"error": "Category cannot be deleted because it includes one or more cocktails."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CocktailViewSet(ModelViewSet):
    queryset = Cocktail.objects.select_related("category").all()
    serializer_class = CocktailSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CocktailFilter
    pagination_class = DefaultPagination
    search_fields = ["name", "ingredients", "directions"]
    ordering_fields = ["name", "category"]

    def get_serializer_context(self):
        return {"request": self.request}

    def delete(self, request, id):
        cocktail = get_object_or_404(Cocktail, pk=id)
        cocktail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)