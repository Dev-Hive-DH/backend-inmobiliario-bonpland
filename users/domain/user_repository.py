# Django
from django.contrib.auth import get_user_model


class UserRepository:
    
    def __init__(self, name=None, surname=None, email=None, phone_number=None, password=None) -> None:
        self.name = name
        self.surname = surname
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.model = get_user_model()

    def create_user(self):
        instance = self.model.objects.create_user(
            name=self.name,
            surname=self.surname,
            email=self.email,
            phone_number=self.phone_number,
            password=self.password,
        )
        instance.save()
        return instance

    def get_by_id(self, id=None):
        return self.model.objects.filter(is_active=True, id=id).only('name', 'surname', 'email', 'phone_number').first()
    
    def get_by_only_id(self, id=None):
        return self.model.objects.filter(is_active=True, id=id).only('id').first()

    def update(self, instance=None, data=None):
        for key, value in data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def update_password(self, id=None, new_password=None):
        instance = self.model.objects.filter(is_active=True, id=id).only('password').first()
        instance.set_password(new_password)
        instance.save()
        return instance
        
    def delete(self, id=None):
        instance = self.model.objects.filter(is_active=True, id=id).only('is_active').first()
        instance.is_active = False
        instance.save()
        return instance



