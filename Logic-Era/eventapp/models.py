from django.db import models

# Create your models here.
class event(models.Model):
    title = models.CharField(max_length=255, null=True)
    date = models.DateTimeField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)
    max = models.IntegerField(null=True)
    description = models.CharField(max_length=2500,null=True)
    banner = models.CharField(max_length=2500,null=True)
    
    def __str__(self):
        return self.title

class user(models.Model):
    name = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.name

class joinevent(models.Model):
  
    Event = models.ForeignKey(event, null=True, on_delete= models.SET_NULL)
    User = models.ForeignKey(user, null=True, on_delete= models.SET_NULL)
    

