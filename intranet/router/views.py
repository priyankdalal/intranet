from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Routers

# Create your views here.
def index(request):
    all_routers=Routers.objects.all()
    context={
        "title": "Intranet - Router",
        "routers":all_routers,
    }
    return render(request,'router/index.html', context)
def addRouter(request):
    if request.is_ajax():
        if "name" in request.POST:
            router=Routers(name=request.POST["name"])
            router.save()
            return JsonResponse({"error":False,"response":"Router created successfully."})
        else:
            return JsonResponse({"error":True,"msg":"No/Invalid Router name."})
    else:
        JsonResponse({"error":True,"msg":"Invalid protocol."})
def removeRouter(request):
    if request.is_ajax():
        if 'id' in request.POST:
            router=Routers.objects.get(id=request.POST["id"])
            router.delete()
            return JsonResponse({"error":False,"response":"Router deleted successfully."})
        else:
            return JsonResponse({"error":True,"msg":"No/Invalid Router."})
    else:
        return JsonResponse({"error":True,"msg":"Invalid protocol."})