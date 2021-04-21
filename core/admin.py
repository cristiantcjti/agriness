from django.contrib import admin
from .models import Client, Book, BookReservations

# Register your models here.

admin.site.register(Client)
admin.site.register(Book)
admin.site.register(BookReservations)