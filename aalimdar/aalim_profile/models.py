from django.db import models

# Create your models here.

class AalimProfile(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/aalim_images/', blank=True, null=True)
    dob = models.CharField( max_length=50,blank=True, null=True)
    dod = models.CharField( max_length=50,blank=True, null=True)
    biography = models.TextField()  
    education = models.TextField(blank=True, null=True)  
    notable_contributions = models.TextField(blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    @property
    def book(self):
        return self.books.all()
    
    @property
    def poetry(self):
        return self.poetry.all()
