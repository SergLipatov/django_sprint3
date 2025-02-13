from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Category, Post, Location

admin.site.empty_value_display = 'Не задано'
Group._meta.verbose_name = "группа"
Group._meta.verbose_name_plural = "Группы"
User._meta.verbose_name = "пользователь"
User._meta.verbose_name_plural = "Пользователи"

class PostInline(admin.TabularInline):
    model = Post
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    #inlines = [PostInline]
    list_display = ('title', 'description', 'slug', 'is_published', 'created_at')
    list_editable = ('is_published',)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    list_editable = ('is_published',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'category', 'location', 'created_at', 'pub_date')
    list_editable = ('is_published',)
    #search_fields = ('title',)
    #list_filter = ('is_published',)
    #list_display_links = ('title',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)