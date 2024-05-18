from django.contrib import admin

from .models import Category, Location, Post

admin.site.empty_value_display = 'Не задано'


class PostInline(admin.StackedInline):
    """Задаем отображение записей в админзоне столбом."""
    model = Post
    extra = 0


class LocationAdmin(admin.ModelAdmin):
    """Переопределяем настройки интерфейса админки для модели локаций."""
    inlines = (
        PostInline,
    )


class CategoryAdmin(admin.ModelAdmin):
    """Переопределяем настройки интерфейса админки для модели категорий."""
    inlines = (
        PostInline,
    )


class PostAdmin(admin.ModelAdmin):
    """Переопределяем настройки интерфейса админки для модели постов."""
    list_display = (
        'title',
        'text',
        'pub_date',
        'author',
        'location',
        'category',
        'is_published',
        'created_at',
    )
    list_editable = (
        'pub_date',
        'is_published',
        'location',
        'category',
    )
    search_fields = ('title',)
    list_filter = ('is_published',)
    list_display_links = ('title',)


admin.site.register(Category, CategoryAdmin)

admin.site.register(Location, LocationAdmin)

admin.site.register(Post, PostAdmin)
