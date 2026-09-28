from django.urls import path

from .views import (
    CreateRecipeView,
    DeleteRecipeView,
    DetailRecipeView,
    RecipesListView,
    UpdateRecipeView,
    main_view,
)

app_name = "recipes"

urlpatterns = [
    path("", main_view, name="main"),
    path("create/", CreateRecipeView.as_view(), name="create"),
    path("recipes/", RecipesListView.as_view(), name="recipes"),
    path("recipes/recipe_<int:pk>/", DetailRecipeView.as_view(), name="detail"),
    path("recipes/recipe_<int:pk>/update", UpdateRecipeView.as_view(), name="update"),
    path("recipes/recipe_<int:pk>/delete", DeleteRecipeView.as_view(), name="delete"),
]
