from django.shortcuts import render
from django.http import JsonResponse
from .models import Plans

# Create your views here.
def index(request):
    plans=Plans.objects.all()
    context={
        'title':'Intranet - Plans',
        'plans':plans,
    }
    return render(request,'plans/index.html',context)
def addPlan(request):
    if request.is_ajax():
        if 'name' in request.POST and 'price' in request.POST :
            plan=Plans(name=request.POST['name'],price=request.POST['price'])
            if 'discount' in request.POST:
                plan.discount=request.POST['discount']
            plan.save()
            return JsonResponse({"error":False,"response":"Plan created successfully."})
        else:
            return JsonResponse({"error":True,"msg":"No/Malformed Plan."})
    else:
        return JsonResponse({"error":True,"msg":"Invalid protocol."})
        