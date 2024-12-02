from django.db import models
from aalim_profile.models import AalimProfile

# Create your models here.

class Poetry(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey(AalimProfile , on_delete=models.CASCADE, related_name='poetry')
    lines = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title