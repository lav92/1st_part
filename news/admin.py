from django.contrib import admin
from .models import News, Category
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'category', 'title', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_editable = ('is_published', )
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
