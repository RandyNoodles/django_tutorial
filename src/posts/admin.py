from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    filter_horizontal = ['liked']  # This enables proper many-to-many editing