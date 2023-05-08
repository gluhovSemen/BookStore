from django.urls import path
from book.views import BookList, BookDetail, AuthorList, PublisherList


urlpatterns = [
    path('books/', BookList.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book_detail'),
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('publishers/', PublisherList.as_view(), name='publisher_list'),
]
