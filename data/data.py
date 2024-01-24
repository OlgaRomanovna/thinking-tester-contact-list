from faker import Faker

fake = Faker()
first_name_for_register = f'{fake.name()}'
last_name_for_register = f'{fake.last_name()}'
email_for_register = f'{fake.email()}'
password = '1234567'


first_name = 'Alexander'
last_name = 'Pushkin'
birthdate = '1799-06-06'
email = 'alexander_pushkin@gmail.com'
phone = '8005555555'
street1 = 'street Glinka'
street2 = 'house 5, flat 17'
city = 'Moscow'
state_province = 'RU'
postal_code = '12345'
country = 'Russia'
