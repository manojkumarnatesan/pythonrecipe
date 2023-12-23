"""URL mapping for the user API"""

from django.urls import path
from .views import CreateUserView,CreateTokenView,ManageUserView

app_name = "user"

urlpatterns = [
    path("signup", CreateUserView.as_view(), name="signup"),
    path("login", CreateTokenView.as_view(), name="login"),
    path("me", ManageUserView.as_view(), name="me"),
]
