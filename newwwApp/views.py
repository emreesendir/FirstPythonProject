from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hi(request):
    return HttpResponse('<h1>HELLO! THIS IS MY HOME PAGE</h1>')