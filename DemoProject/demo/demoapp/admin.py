from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import student

# Register your models here.
# admin.site.register(Members)
@admin.register(student)
class Members(admin.ModelAdmin):
    list_display = ['id','firstname','lastname','contact','address']
