import json
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Zones
# Create your views here.

def index(request):
    all_zones=Zones.objects.all()
    context={
            "title":"Intranet - Zones",
            "zones":all_zones,
    }
    return render(request,'zones/index.html',context)
def addZone(request):
    if request.is_ajax():
        if 'name' in request.POST:
            zone=Zones(name=request.POST['name'])
            zone.save()
            return JsonResponse({"error":False,"response":"Zone created successfully."})
        else:
            return JsonResponse({"error":True,"msg":"No/Invalid zone name."})
    else:
        return JsonResponse({"error":True,"msg":"Invalid protocol"})
def removeZone(request):
    if request.is_ajax():
        if 'id' in request.POST:
            zone=Zones.objects.get(id=request.POST["id"])
            zone.delete();
            return JsonResponse({"error":False,"response":"Zone Deleted successfully."})
        else:
            return JsonResponse({"error":True,"msg":"No/Invalid zone."})
    else:
        return JsonResponse({"error":True,"msg":"Invalid protocol"})
