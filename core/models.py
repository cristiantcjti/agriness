from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

# Create your models here.


class Client(models.Model):    
    id_client = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

class Book(models.Model):
    id_book = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.title        
    
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

class Moviments(models.Model):
    id_moviment = models.AutoField(primary_key=True)
    id_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reserved_for = models.ForeignKey(Client, on_delete=models.CASCADE)
    borrowed_for = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_reserved = models.DateField(null=True, blank=True)
    dete_lent = models.TimeField(null=True, blank=True)
    dete_returned = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.id        
    
    class Meta:
        verbose_name = "Moviment"
        verbose_name_plural = "Moviments"