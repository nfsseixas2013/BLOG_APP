from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>  Welcome to Sure_is Blog <h1>")

def about(request):
    return HttpResponse("<h1>  What about what??? <h1>")

# Create your views here.
