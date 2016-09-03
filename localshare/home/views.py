import datetime
from django.shortcuts import render
from home.models import Event
from django.http import Http404


def index(request):
	try:
		context = Event.objects()
	except:
		raise Http404("No events")
	return render(request, 'index.html',  {'events' : context})

