# Django REST Framework
from rest_framework import serializers

# Django
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

# Python
import re

# Project
from users.domain.user_repository import UserRepository


class CreateUserSerializer(serializers.ModelSerializer):
    
    password_confirm = serializers.CharField(
        max_length=30,
        min_length=8,
        write_only=True,
        style={
            'input_type':'password',
        },
    )
    password = serializers.CharField(
        max_length=30,
        min_length=8,
        write_only=True,
        style={
            'input_type':'password',
        },
    )
    
    class Meta:
        
        model = get_user_model()
        fields = ['name', 'surname', 'email', 'phone_number', 'password', 'password_confirm']
    
    # Validations
    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(
                detail=_(str(e)),
                code=_('Invalid_data')
            )
        return value
    
    def validate(self, data):
        password1 = data['password']
        password2 = data['password_confirm']
        if password1 != password2:
            raise serializers.ValidationError(
                detail={
                    'password':_('The two password fields didn’t match.')
                },
                code=_('Invalid_data')
            )
        return data
    
    # Methods
    def create(self, validated_data):
        user = UserRepository(
            name = validated_data['name'],
            surname = validated_data['surname'],
            email = validated_data['email'],
            phone_number = validated_data['phone_number'],
            password = validated_data['password'],
        )
        return user.create_user()



