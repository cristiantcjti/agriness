from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

# Create your models here.


class Client(models.Model):    
    id_client = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=70)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

class Book(models.Model):
    id_book = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=15, default='disponível')
    def __str__(self):
        return self.title        
    
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

class BookReservations(models.Model):
    id_reservation = models.AutoField(primary_key=True)
    id_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    value = models.FloatField(null=True)
    date_lent = models.DateField(null=True, blank=True)
    date_returned = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.id_reservation)
    
    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"