# setup_test_data.py
import random

from django.db import transaction
from django.core.management.base import BaseCommand

from employees.models import Subdivision, Employee
from employees.factories import SubdivisionFactory, EmployeeFactory


NUM_EMPLOYEES = 50000
NUM_SUBDIVISIONS = 25
NUM_SUBDIVISIONS_LEVELS = 5


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Subdivision, Employee]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        subdivisions_parents = []
        for _ in range(NUM_SUBDIVISIONS_LEVELS):
            subdivision_parent = SubdivisionFactory()
            subdivisions_parents.append(subdivision_parent)

            for _ in range(NUM_SUBDIVISIONS_LEVELS - 1):
                subdivision = SubdivisionFactory(parent=subdivision_parent)
                subdivision_parent = subdivision
                subdivisions_parents.append(subdivision_parent)

        for _ in range(NUM_EMPLOYEES):
            EmployeeFactory(subdivision=random.choice(subdivisions_parents))
