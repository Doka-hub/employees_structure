# Generated by Django 4.1.3 on 2022-11-30 15:19

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subdivision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='employees.subdivision', verbose_name='Родитель')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255, verbose_name='ФИО')),
                ('position', models.CharField(max_length=255, verbose_name='Должность')),
                ('date_joined', models.DateField(verbose_name='Дата приема на работу')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Зарплата')),
                ('subdivision', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='employees.subdivision', verbose_name='Подразделение')),
            ],
        ),
    ]
