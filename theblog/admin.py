from django.contrib import admin
from .models import Post, Category, Profile, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'post_date', 'category', 'isPrivate')
    list_filter = ('author', 'category', 'isPrivate')
    search_fields = ('title', 'body', 'author__username')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'website_url')
    search_fields = ('user__username', 'bio')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'date_added')
    list_filter = ('date_added',)
    search_fields = ('author', 'body', 'post__title')

# Rejestracja modeli z nowymi klasami admina
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Comment, CommentAdmin)
