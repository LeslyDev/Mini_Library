from django.urls import path
from .views import *

# app_name = 'p_library'
urlpatterns = [
    path('', index, name='index_page_url'),
    path('book_increment/', book_increment),
    path('book_decrement/', book_decrement),
    path('author/create', AuthorEdit.as_view(), name='author_create'),
    path('authors', AuthorList.as_view(), name='author_list'),
    path('author/create_many', author_create_many, name='author_create_many'),
    path('author_book/create_many', books_authors_create_many, name='author_book_create_many'),
    path('house/', house, name='house_page_url'),
    path('people/', people, name='people_page_url')
]
