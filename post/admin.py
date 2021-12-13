from django.contrib import admin
from .models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'post_status', 'created_at']
    prepopulated_fields = {'slug': ('title', )}
