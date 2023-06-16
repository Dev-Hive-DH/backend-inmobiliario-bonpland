# Faker
from faker import Faker

# Python
import random


faker = Faker()

class UserFactory:
    
    def build_user_JSON(self) -> dict:
        password = f'Aa{faker.random_number(digits=10)}'
        phone_number_case = [
        f'(+{faker.random_int(min=1, max=999)}){faker.bothify(text="##########")}',
        f'(+{faker.random_int(min=1, max=999)}){faker.bothify(text="### ### ####")}',
        f'(+{faker.random_int(min=1, max=999)}) {faker.bothify(text="### ### ####")}',
        f'(+{faker.random_int(min=1, max=999)}) {faker.bothify(text="##########")}',
        f'(+{faker.random_int(min=1, max=999)}){faker.bothify(text="###-###-####")}',
        f'(+{faker.random_int(min=1, max=999)}) {faker.bothify(text="###-###-####")}',
        ]
        JSON = {
            'name':faker.name(),
            'surname':faker.name(),
            'email':faker.email(),
            'phone_number': random.choice(phone_number_case),
            'password':password,
            'password_confirm':password,
        }
        return JSON



