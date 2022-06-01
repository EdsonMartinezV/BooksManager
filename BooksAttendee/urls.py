from django.urls import path
from . import views

app_name = 'BooksAttendee'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:book_id>/', views.detail, name='detail'),
    path('<int:book_id>/update/', views.update, name='update'),
    path('<int:book_id>/delete/', views.delete, name='delete'),
]
