from django.db import models

# Create your models here.

class Details(models.Model):
    firstname = models.CharField(max_length=50,blank=False,null=False)
    lastname = models.CharField(max_length=50,blank=False,null=False)
    contact = models.IntegerField(blank=False,null=False)
    username = models.CharField(max_length=20,blank=False,null=False)
    
    def __str__(self):
        return self.username
    
    