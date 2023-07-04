from django_filters import FilterSet

from book.models import Book


class BookFilter(FilterSet):
    class Meta:
        model = Book
        fields = ['category', 'price', 'year', 'author']
