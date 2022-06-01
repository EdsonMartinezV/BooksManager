from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from BooksAttendee.models import Book

# Create your views here.
def index(request):
    books_list = Book.objects.order_by('-created_at')
    context = {'books_list': books_list}
    return render(request, 'BooksAttendee/index.html', context)

def create(request):
    if request.method == 'GET':
        return render(request, 'BooksAttendee/create.html')
    elif request.method == 'POST':
        book = Book(title=request.POST['title'], description=request.POST['description'])
        book.save()
        return HttpResponseRedirect(reverse('BooksAttendee:index'))

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'BooksAttendee/detail.html', {'book': book})

def update(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.title = request.POST['title']
    book.description = request.POST['description']
    book.save()
    return HttpResponseRedirect(reverse('BooksAttendee:detail', args=(book.id,)))

def delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return HttpResponseRedirect(reverse('BooksAttendee:index'))
