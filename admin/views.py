from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

# Create your views here.

def test(request):
    return HttpResponse(1)
