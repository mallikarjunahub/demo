from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hai(request):
    return HttpResponse('this is my first fbv')
    
def hello(request):
    return HttpResponse('<h1><marquee>this is my second FBV</marquee></h1>')