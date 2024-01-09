from django.contrib import admin
from django.urls import path
from rest_framework_nested import routers
from . import views

admin.site.site_header = "Cocktails Admin"
admin.site.index_title = "Admin"

router = routers.DefaultRouter()
router.register(r"categories", views.CategoryViewSet, basename="categories")
router.register(r"cocktails", views.CocktailViewSet, basename="cocktails")

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += router.urls