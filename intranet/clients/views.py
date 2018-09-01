from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Clients,Plans,Zones

# Create your views here.
def index(request):
    clients=Clients.objects.all()
    print(clients.query)
    print(clients)
    #clients=Clients.get_clients()
    plans=Clients.get_plans()
    zones=Clients.get_zones()
    context={
        'title':"Intranet - Client",
        'clients':clients,
        'plans':plans,
        'zones':zones
    }
    return render(request,'clients/index.html',context)
def addClient(request):
    if request.is_ajax():
        if 'name' in request.POST and 'mobile' in request.POST and 'plan' in request.POST and 'zone' in request.POST:
            plan=Plans.objects.get(id=request.POST['plan'])
            zone=Zones.objects.get(id=request.POST['zone'])
            client=Clients(
                name=request.POST['name'],
                address=request.POST['address'],
                phone=request.POST['phone'],
                mobile=request.POST['mobile'],
                plan=plan,
                zone=zone,
                type=request.POST['type'],
                pan=request.POST['pan'],
                email=request.POST['email'],
                send_sms=request.POST['sms'],
                comments=request.POST['comments'],
            )
            client.save()
            return JsonResponse({'error':False,'response':'Client created successfully'})
        else:
            return JsonResponse({'error':True,'msg':'No/Malformed client.'})
    else:
        return JsonResponse({"error":True,"msg":"Invalid protocol."})
