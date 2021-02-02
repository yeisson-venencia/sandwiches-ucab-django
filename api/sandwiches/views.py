from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Example' : '/example/',
        'Create': '/create/',
        'Update': '/update/',
        'Delete': '/delete/',
    }

    return Response(api_urls)
