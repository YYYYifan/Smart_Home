from datetime import datetime
from django.core.checks import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import client
import uuid
# Create your views here.

def index(request):
    allClient =  client.objects.all()
    return render(request, 'client/index.html', {'allClient': allClient})


def switch(request, uuid, command):    
    device = client.objects.filter(uuid=uuid)
    device.update(state= True if command == 1 else False)
    context = {        
        'message' : "{}, 设备: {}, 指令:{}".format(timezone.now().strftime("%m月%d日 %H:%M:%S"), device[0].comment, '开' if command == 1 else '关'),
        'allClient': client.objects.all()
    }
    datetime.now().strptime
    return render(request, 'client/index.html', context)

def controlESP(request, uuid):               
    objClient = client.objects.filter(uuid=uuid)
    objClient.update(lastCommunication = timezone.now())

    return HttpResponse(objClient[0].state)


def addClient(request):    
    if request.method == "POST":
        client.objects.create(
            uuid    =  request.POST.get('UUID'),            
            comment =  request.POST.get('comment')        
        )
        context = {
            'UUID': uuid.uuid1(),
            'Message': "成功"
        }
        return render(request, "client/addClient.html", context)
    elif request.method == "GET":
        context = {
            'UUID': uuid.uuid1(),
        }
        return render(request, "client/addClient.html", context)


def delete(request):
    Message = ''
    if request.method == "POST":        
        client.objects.filter(uuid=request.POST.get('UUID')).delete()
        Message = "成功"
    elif request.method == "GET":
        pass
    allClient =  client.objects.all()
    context = {
        'Message': Message,
        'allClient': allClient
    }
    return render(request, "client/delete.html", context)