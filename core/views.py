from .models import Client, Book, BookReservations
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, date
from django.http import HttpResponse, JsonResponse 
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
import logging

# Create your views here.

#CLIENT'S RESERVATION
@csrf_exempt
@require_http_methods(["GET"]) 
def client_reserved_books(request, id_client):
    try: 
        reserve_info = []
        reservations = BookReservations.objects.filter(id_client=id_client).values()
        for reservation in reservations:
            info = []
            info.append(reservation['id_book_id'])
            info.append(reservation['date_lent'])
            info.append(reservation['date_returned'])
            reserve_info.append(info) 
    except BookReservations.DoesNotExist: 
        return JsonResponse({'message':'There is no reservation to the client.'}, status=status.HTTP_404_NOT_FOUND) 
    
    try:   
        reservation_list = []
        for information in reserve_info:  
            title = Book.objects.get(id_book=information[0])
            date_lent = information[1]
            date_returned = format_date(information[2])
            book_information = {'book':title.title, 'date_lent':date_lent, 'date_returned':date_returned, 'additional_charge':check_date(date_lent)}
            reservation_list.append(book_information)
    except Book.DoesNotExist: 
        return JsonResponse({'message':'There is no book found.'}, status=status.HTTP_404_NOT_FOUND) 

    return JsonResponse(reservation_list, safe=False)

#RESERVATION
@csrf_exempt
@require_http_methods(["POST"]) 
def books_reserve(request, id_book):
    
    data = json.loads(request.body)

    try:
        book = Book.objects.get(id_book=id_book)
    except Book.DoesNotExist:
        return JsonResponse({'message':'There is no registered book with the passed id.'}, status=500) 

    try:
        client = Client.objects.get(id_client=data['id_client'])
    except Book.DoesNotExist:
        return JsonResponse({'message':'There is no registered client with the passed id.'}, status=500) 
    
    if book.status == 'disponível':
        reserve = BookReservations(id_book=book, id_client=client, date_lent=data['date_lent'])
        book.status = 'emprestado'
    else:
        return JsonResponse({'message':'book is already reserved.'}, safe=False)
    
    try:
        reserve.save()    
    except Exception as error:
        logging.error(error)
        return JsonResponse({'message': 'Error when saving reservation information.'}, status=500) 

    try:
        book.save()    
    except Exception as error:
        logging.error(error)
        return JsonResponse({'message': 'Error when saving updated book status.'}, status=500) 

    return JsonResponse({'message': 'Reserve created.'}, safe=False, status=201)

#REGISTERED BOOKS
@csrf_exempt
@require_http_methods(["GET"]) 
def books_list(request):
    try:    
        response = []
        books = Book.objects.all()
        for index in range(len(books)): 
            title = books[index].title
            status = books[index].status
            json_to_return = {"title":title,"status":status}
            response.append(json_to_return)
    except Book.DoesNotExist:
        return JsonResponse({'message': 'There is no registered book.'}, status=status.HTTP_404_NOT_FOUND)

    return JsonResponse(response, safe=False, status=200)

#FORMAT A PASSED DATE
def format_date(date):
    if date == None:
        return '' 
    else:
        return date.strftime('%Y-%m-%d')

#CHECK PERIOD
def check_date(date_lent):
    today = datetime.now()
    days_borrowed = today.day - date_lent.day   
    list_of_charges = [[0,0], [0,0], [0,0], [3,0.2], [5,0.4], [5,0.4], [7,0.6]]
    max_count = len(list_of_charges)
    for i in range(max_count):
        if days_borrowed == i or i > 5 :
            penalty = list_of_charges[i][0]
            interest = list_of_charges[i][1]
            return {'days_overdue':days_borrowed, 'penalty':f'{penalty}%', 'interest_per_day':f'{interest}%'}


