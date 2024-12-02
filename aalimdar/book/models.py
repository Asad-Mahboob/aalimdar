from django.db import models
from aalim_profile.models import AalimProfile

# Create your models here.

class Book(models.Model):
    BOOK_LANG = [
        ( 'English','ENG'),
        ( 'Urdu','UR'),
        ( 'Arabic','AR'),
        ( 'Persian','PR'),
    ]
    BOOK_GENRE = [
    ('FIQH', 'Fiqh'),
    ('AQEEDAH', 'Aqeedah'),
    ('POETRY', 'Poetry'),
    ('HIKAYAT', 'Hikayat'),
    ('MASAIL', 'Masail'),
    ]

    title = models.CharField(max_length=200)
    author = models.ForeignKey(AalimProfile, on_delete=models.CASCADE, related_name='books')
    genre = models.CharField( max_length=50,choices=BOOK_GENRE)
    language = models.CharField(max_length=50,choices=BOOK_LANG)
    description = models.TextField(blank=True,null=True)
    publication_date = models.CharField(max_length=200, blank=True, null= True)
    cover_image = models.ImageField(upload_to='photos/book_covers/', blank=True, null=True)
    pdf = models.FileField(upload_to='pdfs/book_pdfs/', blank=True , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
