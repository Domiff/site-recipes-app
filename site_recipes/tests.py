from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from faker import Faker

from site_recipes.models import Category, Recipe

User = get_user_model()
faker = Faker()


class ListDetailRecipeTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username=faker.user_name(),
            password=faker.password(),
            email=faker.email(),
        )
        cls.category1 = Category.objects.create(name=faker.text(100))
        cls.category2 = Category.objects.create(name=faker.text(100))

        cls.recipe = Recipe.objects.create(
            title=faker.text(100),
            description=faker.text(),
            steps=faker.text(),
            time_cooking=faker.text(),
            ingredients=faker.text(),
            image=faker.url(),
            author=cls.user,
        )
        cls.recipe.category.add(
            cls.category1,
            cls.category2,
        )

    def test_list(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("site_recipes:recipes"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.recipe.title)

    def test_detail(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("site_recipes:detail", args=[self.recipe.id])
        )
        self.assertEqual(response.status_code, 200)


class CreateUpdateRecipeTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username=faker.user_name(),
            password=faker.password(),
            email=faker.email(),
        )
        cls.category = Category.objects.create(name=faker.text(100))
        cls.create_data = {
            "title": faker.text(100),
            "description": faker.text(),
            "steps": faker.text(),
            "time_cooking": faker.text(),
            "ingredients": faker.text(),
            "category": cls.category.pk,
        }
        cls.update_data = {
            "title": faker.text(100),
            "description": faker.text(),
            "steps": faker.text(),
            "time_cooking": faker.text(),
            "ingredients": faker.text(),
            "category": cls.category.pk,
        }

    def test_create(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("site_recipes:create"),
            data=self.create_data,
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            Recipe.objects.count(),
            1,
        )

    def test_update(self):
        self.client.force_login(self.user)
        recipe = Recipe.objects.create(
            title=faker.text(100),
            description=faker.text(),
            steps=faker.text(),
            time_cooking=faker.text(),
            ingredients=faker.text(),
            image=faker.url(),
            author=self.user,
        )
        recipe.category.add(self.category)
        response = self.client.post(
            reverse("site_recipes:update", args=[recipe.pk]),
            data=self.update_data,
        )
        self.assertEqual(response.status_code, 302)


class DeleteRecipeTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username=faker.user_name(),
            password=faker.password(),
            email=faker.email(),
        )
        cls.recipe = Recipe.objects.create(
            title=faker.text(100),
            description=faker.text(),
            steps=faker.text(),
            time_cooking=faker.text(),
            ingredients=faker.text(),
            image=faker.url(),
            author=cls.user,
        )

    def test_delete(self):
        self.client.force_login(self.user)
        response = self.client.delete(
            reverse("site_recipes:delete", args=[self.recipe.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            Recipe.objects.count(),
            0,
        )
