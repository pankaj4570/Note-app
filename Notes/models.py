# Create your models here.

from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return  self.title


