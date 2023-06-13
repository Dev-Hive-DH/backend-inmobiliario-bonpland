# Django
from django.urls import path

# Project
from users.infrastructure.views import (
    CreateUserAPIView,
)


urlpatterns = [
    path('api/create-user/', CreateUserAPIView.as_view(), name='create_user'),
]