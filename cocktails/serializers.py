from rest_framework import serializers
from .models import Category, Cocktail

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "cocktails_count"]

    cocktails_count = serializers.IntegerField(read_only=True)

class CocktailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = Cocktail
        fields = ["id", "name", "ingredients", "directions", "photo_url", "category"]