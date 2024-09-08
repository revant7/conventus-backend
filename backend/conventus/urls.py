from django.urls import path
from .views import RegistrationView, ContactResponseView

urlpatterns = [
    path("register/", RegistrationView.as_view(), name="register"),
    path("contact/", ContactResponseView.as_view(), name="contact"),
]
