from django.contrib import admin

from .models import Subdivision, Employee


@admin.register(Subdivision)
class SubdivisionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'parent',
    ]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'fullname',
        'position',
        'date_joined',
        'salary',
        'subdivision',
    ]
    list_filter = [
        'subdivision__id'
    ]
