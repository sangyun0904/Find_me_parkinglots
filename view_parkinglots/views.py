import csv 
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    response = HttpResponse(
        content_type="text/csv" , 
        headers={'Content-Disposition' : 'attachment; filename="'}
    )

    return render(request, "index.html")
