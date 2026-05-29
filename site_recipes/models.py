from django.contrib.auth.models import User
from django.db import models


def image_directory(instance: "Recipe", filename: str) -> str:
    return "recipes/preview/{filename}".format(
        pk=instance.pk, filename=filename
    )


class Recipe(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="Название блюда")
    description = models.TextField(null=False, blank=False, verbose_name="Описание блюда")
    steps = models.TextField(null=False, blank=False, verbose_name="Шаги приготовления блюда")
    time_cooking = models.CharField(null=False, blank=False, verbose_name="Время приготовления блюда")
    ingredients = models.TextField(null=False, blank=False, verbose_name="Ингредиенты для блюда")
    image = models.ImageField(null=True, blank=True, upload_to=image_directory, verbose_name="Изображение блюда")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор рецепта")
    category = models.ManyToManyField("Category", verbose_name="Категория")

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Категория")

    def __str__(self):
        return self.name
