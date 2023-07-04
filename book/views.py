from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from book.models import Book
from book.serializers import BookSerializer, BookDetailSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from book.filters import BookFilter


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'year', 'author')
    filterset_class = BookFilter

    def retrieve(self, request, *args, **kwargs):
        self.get_queryset()
        instance = self.get_object()
        instance.view_count += 1
        instance.save()
        serializer = BookDetailSerializer(instance)
        return Response(serializer.data)
