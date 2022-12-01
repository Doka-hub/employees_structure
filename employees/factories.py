import factory
from factory.django import DjangoModelFactory

from .models import Subdivision, Employee


class SubdivisionFactory(DjangoModelFactory):
    name = factory.Faker('job')
    # parent = factory.SubFactory('SubdivisionFactory')

    class Meta:
        model = Subdivision


class EmployeeFactory(DjangoModelFactory):
    fullname = factory.Faker('name')
    position = factory.Faker('job')
    date_joined = factory.Faker('date_this_century')
    salary = factory.Faker('pydecimal', min_value=100, max_value=5000)

    class Meta:
        model = Employee


