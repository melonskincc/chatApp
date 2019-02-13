from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'chat/index.html', locals())


def room(request, roomName):
    return render(request, 'chat/room.html',locals())