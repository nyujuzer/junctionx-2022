import http
from .models import *
from .serializers import *
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .jsonExtractor import over 

# Create your views here.

def index(request):
    return HttpResponse("Welcome to GettingWise by team that does not have a name yet!")

def merchant(request):
    merchants = known_vendors.objects.all()
    serializer = merchantSerializer(merchants, many=True)
    return JsonResponse(serializer.data, safe=False)

def resultofmerchant(request, merchant(request)):
    return render(request, 'result-display.html')
