# Django REST Framework
from rest_framework.response import Response
from rest_framework import (
    generics, status,
)

# Django
from django.utils.translation import gettext_lazy as _

# Project
from users.infrastructure.serializers import CreateUserSerializer


class CreateUserAPIView(generics.GenericAPIView):
    
    serializer_class = CreateUserSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {
                'message':_('Registration successful.'),
            }
            return Response(message, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
