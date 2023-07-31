from django.shortcuts import render
from math import sin
# Create your views here.

def start_page(request):
    return render(request,'about.html')