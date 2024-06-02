from django.contrib import admin
from .models import Orphan

@admin.register(Orphan)
class OrphanAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'date_of_birth')
