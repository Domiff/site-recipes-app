from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from faker import Faker

User = get_user_model()
faker = Faker()


class RegisterUserTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.password = faker.password()
        cls.credentials = {
            "username": faker.user_name(),
            "email": faker.email(),
            "password1": cls.password,
            "password2": cls.password,
        }

    def test_register(self):
        response = self.client.post(
            path=reverse("auth_user:register"), data=self.credentials
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            User.objects.count(),
            1,
        )


class LoginUserTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.credentials = {
            "username": faker.user_name(),
            "password": faker.password(),
        }
        cls.user = User.objects.create_user(
            username=cls.credentials["username"],
            password=cls.credentials["password"],
        )

    def test_login(self):
        response = self.client.post(
            path=reverse("auth_user:login"), data=self.credentials
        )
        self.assertEqual(response.status_code, 302)


class LogoutUserTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username=faker.user_name(),
            password=faker.password(),
            email=faker.email(),
        )

    def test_logout(self):
        response = self.client.post(path=reverse("auth_user:logout"))
        self.assertEqual(response.status_code, 302)
