from django.contrib import admin
from Blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'counted_views', 'created_date', 'published_date')
    list_filter = ('status', 'created_date')
    search_fields = ('title', 'content')
