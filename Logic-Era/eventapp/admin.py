from django.contrib import admin
from .models import event
from .models import joinevent
from .models import user

# Register your models here.
admin.site.register(event)
admin.site.register(joinevent)
admin.site.register(user)