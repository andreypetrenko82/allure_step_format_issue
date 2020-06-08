import allure
from behave import step
from faker import Faker

fake = Faker(['en_US'])


@step('I specify "{random_name}" as user name')
def step_impl(context, random_name):
    user_name = fake.first_name_male()  # Faker method: https://faker.readthedocs.io/en/master/locales/en_US.html#faker-providers-person
    context.step.name = context.step.name.format(random_name=user_name)
    allure.attach(user_name, 'User name')

@step('I specify "{random_email}" as user email')
def step_impl(context, random_email):
    email = fake.email()
    context.step.name = context.step.name.format(random_email=email)
    assert 2+2 == 4, 'Error: incorrect result'

@step('I specify "{random_phone}" as user phone number')
def step_impl(context, random_phone):
    phone = fake.phone_number()
    context.step.name = context.step.name.format(random_phone=phone)

@step('click "Save" button')
def step_impl(context):
    pass
