from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {}
    return (render(request, 'index.html', context))

def create_list(request):
    if (request.method == 'POST'):
        return (HttpResponse("POST was sent"))
    elif (request.method == 'GET'):
        return (HttpResponse("GET was sent"))
    else:
        return ("Error")