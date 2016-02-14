from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    context = {    
        'request' : request,   
        'lat_data': -34.397, 
        'lng_data': 150.644,
    }
    return render(request, 'home.html', context)