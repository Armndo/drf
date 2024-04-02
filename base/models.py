from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    age = models.SmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name