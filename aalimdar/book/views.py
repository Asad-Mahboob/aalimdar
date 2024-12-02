from django.shortcuts import render, get_object_or_404
from .models import Book
from aalim_profile.models import AalimProfile

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)    
    return render(request, 'book_detail.html', {'book': book, })
