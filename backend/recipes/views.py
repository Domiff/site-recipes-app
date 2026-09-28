from random import sample

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import RecipeForm, RecipeUpdateForm
from .mixins import AuthorRequiredMixin
from .models import Recipe


def main_view(request):
    template_name = "recipes/main.html"
    queryset = list(Recipe.objects.all())
    if queryset:
        random_recipes = sample(queryset, 5)
        context = {
            "random_recipes": random_recipes,
        }
        return render(request, template_name, context)
    return render(request, template_name)


class RecipesListView(ListView):
    model = Recipe
    context_object_name = "recipes"
    queryset = Recipe.objects.all()
    template_name = "recipes/recipes_list.html"


class CreateRecipeView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipes/recipe_create.html"
    success_url = reverse_lazy("recipes:recipes")
    login_url = reverse_lazy("auth_user:login")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DetailRecipeView(DetailView):
    template_name = "recipes/recipe_detail.html"
    context_object_name = "recipe"

    def get_object(self, queryset=None):
        return Recipe.objects.prefetch_related("category").get(pk=self.kwargs["pk"])


class UpdateRecipeView(LoginRequiredMixin, AuthorRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeUpdateForm
    template_name = "recipes/recipe_update.html"
    success_url = reverse_lazy("recipes:detail")
    context_object_name = "recipe"
    login_url = reverse_lazy("auth_user:login")

    def get_object(self, queryset=None):
        return Recipe.objects.prefetch_related("category").get(pk=self.kwargs["pk"])

    def get_success_url(self):
        return reverse_lazy("recipes:detail", kwargs={"pk": self.kwargs["pk"]})


class DeleteRecipeView(LoginRequiredMixin, AuthorRequiredMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy("recipes:recipes")
    login_url = reverse_lazy("auth_user:login")
