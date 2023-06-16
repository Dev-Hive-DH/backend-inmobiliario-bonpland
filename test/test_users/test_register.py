# Django REST Framework
from rest_framework.test import APITestCase
from rest_framework import status

# Django
from django.contrib.auth import get_user_model
from django.urls import reverse

# Faker
from faker import Faker

# Project
from test.factories.users.user_factory import UserFactory


faker = Faker()

class TestUserRegistration(APITestCase):
    
    def setUp(self) -> None:
        self.url = reverse('create_user')
        return super().setUp()
    
    def test_create_user(self) -> None:
        # The status code of the request is checked
        JSON = UserFactory().build_user_JSON()
        response = self.client.post(self.url, JSON, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # The user's existence is verified
        user_exists = get_user_model().objects.filter(email=JSON['email']).exists()
        self.assertTrue(user_exists)
        
        # User data is verifiedgit 
        user = get_user_model().objects.get(email=JSON['email'])
        self.assertEqual(user.name, JSON['name'])
        self.assertEqual(user.surname, JSON['surname'])
        self.assertEqual(user.email, JSON['email'])
        self.assertEqual(user.phone_number, JSON['phone_number'])
        self.assertTrue(user.check_password(JSON['password']))

    def test_if_send_empty_JSON(self):
        JSON = {}
        response = self.client.post(self.url, JSON, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(email='').exists()
        self.assertFalse(user_exists)

    def test_if_passwords_dont_match(self):
        JSON = UserFactory().build_user_JSON()
        JSON['password_confirm'] = password = faker.random_number(digits=10)
        response = self.client.post(self.url, JSON, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(email=JSON['email']).exists()
        self.assertFalse(user_exists)
    
    def test_if_JSON_data_is_invalid(self):
        invalid_email = [
            'email@.com',
            'email@.1',
            'email@com',
            'email@',
            'email@1',
            'email@gmail',
            'email.com',
            'email@gmail.c',
            'email',
            'email@gmail.com.c',
        ]
        invalid_phone_number = [
            '+5731111',
            '+57 31111',
            '+573111111111111',
            '5731111',
            '()2154211',
        ]
        invalid_name_surname = [
            'Carlos 2023',
            '2023',
            'sebastian_moreno',
            'valentina.forero',
            'Juan@andres',
            '@Juan',
            'juan007',
            'cristian.'
            'sonia(ariza)',
        ]
        JSON = UserFactory().build_user_JSON()
        for element in invalid_email:
            JSON['email'] = element
            response = self.client.post(self.url, JSON, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            user_exists = get_user_model().objects.filter(email=JSON['email']).exists()
            self.assertFalse(user_exists)
        JSON = UserFactory().build_user_JSON()
        for element in invalid_phone_number:
            JSON['phone_number'] = element
            response = self.client.post(self.url, JSON, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            user_exists = get_user_model().objects.filter(email=JSON['email']).exists()
            self.assertFalse(user_exists)
        JSON = UserFactory().build_user_JSON()
        for element in invalid_name_surname:
            JSON['name'] = element
            response = self.client.post(self.url, JSON, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            user_exists = get_user_model().objects.filter(email=JSON['email']).exists()
            self.assertFalse(user_exists)
        JSON = UserFactory().build_user_JSON()
        for element in invalid_name_surname:
            JSON['surname'] = element
            response = self.client.post(self.url, JSON, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            user_exists = get_user_model().objects.filter(email=JSON['email']).exists()
            self.assertFalse(user_exists)

