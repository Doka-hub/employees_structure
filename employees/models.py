from django.db import models


from mptt.models import MPTTModel, TreeForeignKey


class Subdivision(MPTTModel):
    name = models.CharField(max_length=255, verbose_name='Название')
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        blank=True,
        null=True,
        verbose_name='Родитель',
    )

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    def __str__(self):
        pre = f'{self.parent} | ' if self.parent else ''
        return f'{pre}{self.name} | {self.name}'

    def get_employees(self):
        return [
            {
                'fullname': employee.fullname,
                'position': employee.position,
                'date_joined': employee.date_joined,
                'salary': employee.salary,
            } for employee in self.employees.all()
        ]

    def get_children_data(self):
        return [
            {
                'id': child.id,
                'name': child.name,
                'children': child.get_children_data(),
            } for child in self.children.all()
        ]

    @classmethod
    def get_data(cls):
        data = [
            {
                'id': subdivision.id,
                'name': subdivision.name,
                'children': subdivision.get_children_data()
            } for subdivision in cls.objects.filter(parent__isnull=True)
        ]
        return data


class Employee(models.Model):
    fullname = models.CharField(max_length=255, verbose_name='ФИО')
    position = models.CharField(max_length=255, verbose_name='Должность')
    date_joined = models.DateField(verbose_name='Дата приема на работу')
    salary = models.DecimalField(max_digits=100, decimal_places=2, verbose_name='Зарплата')
    subdivision = TreeForeignKey(Subdivision, on_delete=models.CASCADE, related_name='employees',
                                 blank=True, null=True,
                                 verbose_name='Подразделение')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.fullname
