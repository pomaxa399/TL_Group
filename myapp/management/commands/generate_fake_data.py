from django.core.management.base import BaseCommand
from faker import Faker
import random
from myapp.models import Employee, Department


class Command(BaseCommand):
    help = 'Generate fake data for testing'

    def handle(self, *args, **kwargs):
        fake = Faker('ru_RU')
        departments = []

        # Количество подразделений на каждом уровне
        level_distribution = [1, 4, 5, 6, 9]

        # Проверка, что распределение уровней корректно
        assert sum(level_distribution) == 25, "Общее количество подразделений должно быть равно 25"

        # Создание подразделений с уровнями
        current_level = 0
        for level_count in level_distribution:
            new_departments = []
            for _ in range(level_count):
                if current_level == 0:
                    parent = None
                else:
                    parent = random.choice(departments)
                department = Department.objects.create(name=fake.company(), parent=parent, level=current_level)
                new_departments.append(department)
            departments.extend(new_departments)
            current_level += 1

        # Создание сотрудников
        for _ in range(50000):
            Employee.objects.create(
                name=fake.name(),
                position=fake.job(),
                hire_date=fake.date_this_century(),
                salary=round(random.uniform(30000, 200000), 2),
                department=random.choice(departments)
            )

        self.stdout.write(self.style.SUCCESS('Successfully generated fake data'))
