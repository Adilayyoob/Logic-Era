from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.


def main(request):
    return render(request, 'accounts/main.html')

def home(request):
    events = event.objects.all()
    return render(request, 'accounts/home.html',{'events':events})

def create(request):
    return render(request, 'accounts/create.html')

def join(request,us):
    users = user.objects.get(id=us)
    events = event.objects.all()
    joinevents = joinevent.objects.all()
    usersJoinedEvent = users.joinevent_set.all()
    context = {
        'events':events,
        'joinevents':joinevents,
        'users':users,
        'usersJoinedEvent':usersJoinedEvent,
    }
    return render(request, 'accounts/join.html', context)



