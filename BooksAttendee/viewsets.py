from rest_framework import viewsets
from .serializers import BookSerializer
from BooksAttendee.models import Book

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer