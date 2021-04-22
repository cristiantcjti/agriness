from django.db.utils import IntegrityError
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse 
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Client, Book, BookReservations
import json
from datetime import date

# Create your views here.

@csrf_exempt
@require_http_methods(["GET"]) 
def client_reserved_books(request, id_client):
    try: 
        reserve_info = []
        reservations = BookReservations.objects.filter(id_client=id_client).values()
        for reservation in reservations:
            info = []
            info.append(reservation['id_book_id'])
            info.append(check_date(reservation['date_lent']))
            info.append(check_date(reservation['date_returned']))
            reserve_info.append(info) 
    except BookReservations.DoesNotExist: 
        return JsonResponse({'message': 'There is no reservation to the client.'}, status=status.HTTP_404_NOT_FOUND) 
    try:   
        reservation_list = []
        print('size...:', len(reserve_info)) 
        for info in reserve_info:  
            book_information = [] 
            title = Book.objects.get(id_book=info[0])
            date_lent = info[1]
            date_returned = info[2]
#            book_information.append(title.title)
#            book_information.append(date)
            book_information = {'Book': title.title, 'Date lent': date_lent, 'Date returned': date_returned, 'Additional charge': ''}
#            reservation_list.append(book_information)
            reservation_list.append(book_information)

    except Book.DoesNotExist: 
        return JsonResponse({'message': 'There is no book to the client.'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == "GET":
        return JsonResponse(reservation_list, safe=False)
    else:
        return HttpResponse("POST")

def check_date(date):
    if date == None:
        return '' 
    else:
        return date.strftime('%m/%d/%Y')



