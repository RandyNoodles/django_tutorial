from django.contrib import admin
from .models import Post, Photo

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    filter_horizontal = ['liked']  # This enables proper many-to-many editing

admin.site.register(Photo)

