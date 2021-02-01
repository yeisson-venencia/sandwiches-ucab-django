from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Hoooome </h1>')

def about(reques):
    return HttpResponse('<h1>About </h1>')