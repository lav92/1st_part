from django import template
from django.db.models import Count

from news.models import Category

register = template.Library()

@register.simple_tag
def get_categories():
    return Category.objects.annotate(count=Count('news'))

