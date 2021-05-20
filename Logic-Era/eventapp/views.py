from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import *
from .form import joineventForm, CreateUserForm, eventForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


def main(request,us):
    users = User.objects.get(id=us)
    
    context = {
         'users':users,
         
    }
    return render(request, 'accounts/main.html', context)

@login_required(login_url='login')
def home(request,us):
    a_user = request.user.id 
    users = User.objects.get(id=us)
    events = event.objects.all()
    joinevents = joinevent.objects.all()
    joinedEventCount = joinevents.filter(User_id=us).count()
    context = {
         'users':users,
         'events':events,
         'joinedEventCount':joinedEventCount,
         'a_user':a_user,
     }
    return render(request, 'accounts/home.html', context)
    
@login_required(login_url='login')
def create(request,us):
    form = eventForm()
    users = User.objects.get(id=us)
    if request.method == 'POST':
        form = eventForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'users':users,
        'form':form,
       
     }
    return render(request, 'accounts/create.html', context)
    
@login_required(login_url='login')
def join(request,us):
    users = User.objects.get(id=us)
    form = joineventForm(initial={'User':users})
    if request.method == 'POST':
        form = joineventForm(request.POST)
        if form.is_valid():
            form.save()
    
    events = event.objects.all()
    joinevents = joinevent.objects.all()
    usersJoinedEvent = users.joinevent_set.all()
    context = {
        'events':events,
        'joinevents':joinevents,
        'users':users,
        'usersJoinedEvent':usersJoinedEvent,
        'form':form,
    }
    return render(request, 'accounts/join.html', context)
@login_required(login_url='login')
def deletejoin(request, us):
    joinevents = joinevent.objects.get(id=us)
    usersid = joinevents.User_id
    users = User.objects.get(id=usersid)
    if request.method == 'POST':
        joinevents.delete()
        return redirect('/join/' + str(usersid))
    context = {
        'users':users,
        'joinevents':joinevents,
     }
    return render(request, 'accounts/deletejoin.html', context)



def register(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Accound was created for ' + user )
                return redirect('login')
    
        context = {
            'form':form
        }
        return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        context = {}
        if request.method  == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
               
    
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home/'  + str(request.user.id))
            else:
                messages.info(request, 'Username OR password is incorrect')
                
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')







