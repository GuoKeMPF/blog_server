from django.contrib import admin

from .models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "author", "create_time", "update_time", "views")
    search_fields = list_display
    list_filter = list_display
