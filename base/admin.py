from django.contrib import admin
from .models import Item, Category

class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "age", "is_underage"]
    

admin.site.register(Item, ItemAdmin)
admin.site.register(Category)

# Register your models here.
