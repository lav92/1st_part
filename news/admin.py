from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'category', 'title', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_editable = ('is_published', )
    list_filter = ('is_published', 'category')
    fields = ('created_at', 'category', 'title', 'content', 'is_published', 'get_photo', 'photo')
    readonly_fields = ('created_at', 'get_photo')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src={obj.photo.url} width=100>')

    get_photo.short_description = 'Фото'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
