from django.shortcuts import render
from .models import *

def index(request):
    context= {
        'books': Book.objects.all(),
    }
        
   
    return render (request, 'pages/index.html', context)

def books(request):
    return render (request, 'pages/books.html')

def delete(request):
    return render (request, 'pages/delete.html')

def update(request):
    return render (request, 'pages/update.html')
def f(request):
    return render (request, 'pages/demo.html')
