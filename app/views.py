# your_app/views.py
from django.shortcuts import render
from app.models import Book

def book_list(request):
    # Query all books with their authors using select_related to reduce queries
    books = Book.objects.select_related('author').all()

    # Pass the books to the template
    return render(request, 'book_list.html', {'books': books})
