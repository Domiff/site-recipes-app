from django.forms import ModelForm, Textarea
from django.forms.widgets import CheckboxSelectMultiple

from .models import Recipe


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "description",
            "image",
            "steps",
            "time_cooking",
            "ingredients",
            "category",
        ]

        widgets = {
            "description": Textarea(attrs={"rows": 6, "cols": 80}),
            "steps": Textarea(attrs={"rows": 6, "cols": 80}),
            "category": CheckboxSelectMultiple(),
        }


class RecipeUpdateForm(ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "description",
            "steps",
            "time_cooking",
            "ingredients",
            "category",
        ]

        widgets = {
            "category": CheckboxSelectMultiple(),
        }
