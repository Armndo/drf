from django.db import models
from django.contrib import admin

# Create your models here.

class Item(models.Model):    
    name = models.CharField(max_length=200)
    age = models.SmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    @admin.display(
        boolean=True,
        ordering="age",
        description="Underage?"
    )
    def is_underage(self):
        return self.age < 18
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
        
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name