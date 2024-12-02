from django.shortcuts import render
from aalim_profile.models import AalimProfile
from book.models import Book
from poetry.models import Poetry
from datetime import datetime

def home(request):
    # Get the current date (to ensure daily changes)
    current_date = datetime.now().strftime('%Y-%m-%d')

    # Select one Aalim based on the current date
    aalims_count = AalimProfile.objects.count()
    aalim_index = int(current_date.replace("-", "")) % aalims_count
    aalim_to_display = AalimProfile.objects.all()[aalim_index]

    # Select one Poetry based on the current date
    poetry_count = Poetry.objects.count()
    poetry_index = int(current_date.replace("-", "")) % poetry_count
    poetry_to_display = Poetry.objects.all()[poetry_index]

    # Select one Book based on the current date
    book_count = Book.objects.count()
    book_index = int(current_date.replace("-", "")) % book_count
    book_to_display = Book.objects.all()[book_index]

    return render(request, 'home.html', {
        'aalim': aalim_to_display,
        'poetry': poetry_to_display,
        'book': book_to_display
    })

def about_us(request):
    return render(request, 'about_us.html')