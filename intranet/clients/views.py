from django.shortcuts import render
from django.http import HttpResponse
from .models import Clients

# Create your views here.
def index(request):
    clients=Clients.objects.all()
    plans=Clients.get_plans()
    zones=Clients.get_zones()
    context={
        'title':"Intranet - Client",
        'clients':clients,
        'plans':plans,
        'zones':zones
    }
    return render(request,'clients/index.html',context)
