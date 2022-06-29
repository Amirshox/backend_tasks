from django.contrib import admin

from .models import Staff


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_date', 'email', 'salary')
    search_fields = ('full_name', 'salary')
    list_editable = ('salary',)
