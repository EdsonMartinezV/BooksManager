from django.urls import path, include
from .models import Book
from . import views
from rest_framework import routers, serializers, viewsets

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)

app_name = 'BooksAttendee'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:book_id>/', views.detail, name='detail'),
    path('<int:book_id>/update/', views.update, name='update'),
    path('<int:book_id>/delete/', views.delete, name='delete'),
    path('api/', include(router.urls))
]
