from django.contrib import admin

# Register your models here.
from .models import Draft

@admin.register(Draft)
class DraftAdmin(admin.ModelAdmin):
    list_display = ('title','content','author','create_time','update_time')
    search_fields = list_display
    list_filter = list_display