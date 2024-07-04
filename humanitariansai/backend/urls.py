from django.urls import path
from .views import HelloWorldView, UserRegistrationView

urlpatterns = [
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
]