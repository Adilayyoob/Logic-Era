from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import *
from .form import joineventForm, CreateUserForm, eventForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def main(request,us):
    users = User.objects.get(id=us)
    
    context = {
         'users':users,
         
    }
    return render(request, 'accounts/main.html', context)

@login_required(login_url='login')
def home(request,us):
    au_user = request.user.id 
    users = User.objects.get(id=us)
    events = event.objects.all()
    joinevents = joinevent.objects.all()
    joinedEventCount = joinevents.filter(User_id=us).count()
    CreatedEventCount = events.filter(a_user=us).count()
    context = {
         'users':users,
         'events':events,
         'joinedEventCount':joinedEventCount,
         'au_user':au_user,
         'CreatedEventCount':CreatedEventCount,
     }
    return render(request, 'accounts/home.html', context)
    
@login_required(login_url='login')
def create(request,us):
    events = event.objects.all()
    form = eventForm(initial={'a_user':request.user.id})
    users = User.objects.get(id=us)
    if request.method == 'POST':
        form = eventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('/create/' + str(request.user.id))
    context = {
        'users':users,
        'form':form,
        'events':events,
       
     }
    return render(request, 'accounts/create.html', context)

@login_required(login_url='login')
def deleteevent(request, us):
    events = event.objects.get(id=us)
    usersid = events.a_user
    users = User.objects.get(id=usersid)
    if request.method == 'POST':
        events.delete()
        return redirect('/create/' + str(request.user.id))
    context = {
        'users':users,
        'events':events,
     }
    return render(request, 'accounts/deleteevent.html', context)
    
@login_required(login_url='login')
def join(request,us):
    events = event.objects.all()
    users = User.objects.get(id=us)
    form = joineventForm(initial={'User':users})
    if request.method == 'POST':
        form = joineventForm(request.POST)
        if form.is_valid():
            form.save()
    
    
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



@login_required(login_url='login')
def eventdetails(request, us):
    events = event.objects.get(id=us)
    usersid = events.a_user
    users = User.objects.get(id=usersid)

    peoplejoined = joinevent.objects.filter(Event_id=us)
    users1 = User.objects.all()
    
    context = {
        'users':users,
        'peoplejoined':peoplejoined,
        'users1':users1,
        'events':events,
    }
    return render(request, 'accounts/eventdetails.html', context)


def welcome(request):
    events = event.objects.latest('id')
    context = {
        'events':events,
    }
    return render(request, 'accounts/welcome.html', context)




def register(request):
    if request.user.is_authenticated:
        return redirect('/home/' + str(request.user.id))
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
        return redirect('/home/' + str(request.user.id))
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








