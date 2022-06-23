from django.contrib import admin
from .models import Data

# Register your models here.
class DataAdmin(admin.ModelAdmin):
    list_display = ('country', 'year', 'category', 'state', 'type', 'consumption')
admin.site.register(Data, DataAdmin)