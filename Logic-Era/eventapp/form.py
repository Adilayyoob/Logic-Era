from django.db.models import fields
from django.forms import ModelForm
from .models import joinevent
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import event

class joineventForm(ModelForm):
    class Meta:
        model = joinevent
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class eventForm(ModelForm):
    class Meta:
        model = event
        fields = '__all__'