from django.shortcuts import render, get_object_or_404
from book.models import Book
from poetry.models import Poetry

def poetry_list(request):
    poetry = Poetry.objects.all()
    return render(request, 'poetry_list.html', {'poetry': poetry})

def poetry_detail(request, pk):
    poetry = get_object_or_404(Poetry, pk=pk)    
    return render(request, 'poetry_detail.html', {'poetry': poetry, })
