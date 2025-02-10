from django.contrib import admin

from .models import Category, Post, Location

admin.site.empty_value_display = 'Не задано'


class PostInline(admin.TabularInline):
    model = Post
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        PostInline,
    ]


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category',
    )
    search_fields = ('title',)
    list_filter = ('is_published',)
    list_display_links = ('title',)
    filter_vertical = ('toppings',)


# Регистрируем класс с настройками админки для моделей IceCream и Category:
admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Topping)
admin.site.register(Wrapper)