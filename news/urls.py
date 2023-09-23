from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', category, name='category'),
    path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/add_news/', add_news, name='add_news'),
]