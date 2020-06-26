from django.http import JsonResponse
from django.shortcuts import render
from .models import Temperature
# Create your views here.

def index(request):
    print('index')
    return render(request, "iot/index.html")

def inputData(request, humi, temp):
    print(humi)
    print(temp)
    # 1. Device name이 DB에 있는지??
    # 2. Device가 없다면, DB저장을 하면 X, return {"result" : "None"}
    # 3. Device가 있다면, DB저장 return {"result" : "success"}

    new_input = Temperature.objects.create(humi=humi, temp=temp)
    return JsonResponse({"result" : "success"}, status=200)


def selectAll(request):

    context={}
    context["results"] = Temperature.objects.all()
    print(context)

    return render(request,"iot/dashboard.html", context)