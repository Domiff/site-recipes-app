from django.urls import path

from .views import (
    RegisterUserView,
    LoginUserView,
    logout_view,
)

app_name = "auth_user_app"

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),
    path(
        "login/", LoginUserView.as_view(redirect_authenticated_user=True), name="login"
    ),
    path("logout/", logout_view, name="logout"),
]
