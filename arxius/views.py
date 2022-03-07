from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
def index(req):
	return HttpResponse("<h1>IetiCloud, el millor Cloud per a tu!</h1><h2>Benvingut a l'index d'arxius</h2>")