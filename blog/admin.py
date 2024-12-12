from django.contrib import admin
from .models import Post, PostCategory
from markdownx.admin import MarkdownxModelAdmin


@admin.register(Post)
class PostAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'author', 'is_published', 'created_at')
    list_filter = ('is_published', 'created_at', 'categories')
    search_fields = ('title', 'content', 'tags', 'author__username')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'color')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
