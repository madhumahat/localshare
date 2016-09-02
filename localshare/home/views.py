import datetime
from django.shortcuts import render


def index(request):
    return render(request, 'index.html',  {'time' : datetime.datetime.now()})
