from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import json


def home(request):
    
    context = {    
        'request' : request,   
        'lat_data': -34.397, 
        'lng_data': 150.644,
    }
    return render(request, 'home.html', context)

def data(request):
    context = {    
        'request' : request,   
        'lat_data': -34.397, 
        'lng_data': 150.644,
    }
    if request.is_ajax():
        if request.method == 'POST':
            # m = (request.body).decode('utf-8')
            # received_json_data=json.loads(m)
            # print('Raw Data: "%s"' % received_json_data)
            m = request.POST['drink']
            print('Raw Data: "%s"' % m)
    return JsonResponse({'foo':'bar'})