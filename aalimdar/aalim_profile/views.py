from django.shortcuts import render, get_object_or_404
from .models import AalimProfile
from book.models import Book
from poetry.models import Poetry

# Create your views here.

def aalim_list(request):
    aalims = AalimProfile.objects.all()
    return render(request, 'aalim_list.html', {'aalims': aalims})


def aalim_detail(request, pk):
    aalim = get_object_or_404(AalimProfile, pk=pk)
    books = Book.objects.filter(author=aalim)
    poetry = Poetry.objects.filter(author=aalim)
    

    return render(request, 'aalim_detail.html', {
        'aalim': aalim,
        'books': books,
        'poetry': poetry,
    })
