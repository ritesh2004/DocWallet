from django.db import models

# Create your models here.

class Details(models.Model):
    username = models.CharField(max_length=20,blank=False,null=False)
    fingerprint = models.CharField(max_length=50,blank=False,null=False)
    
    def __str__(self):
        return self.username
   
   
class AadhaarDetails(models.Model):
    firstname = models.CharField(max_length=50,blank=False,null=False)
    lastname = models.CharField(max_length=50,blank=False,null=False)
    gender = models.CharField(max_length=12,blank=False,null=False)
    aadhar_no = models.BigIntegerField(blank=False,null=False)
    dob = models.DateField(blank=False,null=False)
    image = models.FileField(blank=False,null=False, upload_to='upload/images')
    
    def __str__(self):
        return self.firstname
    
    
class PANdetails(models.Model):
    firstname = models.CharField(max_length=50,blank=False,null=False)
    lastname = models.CharField(max_length=50,blank=False,null=False)
    gender = models.CharField(max_length=12,blank=False,null=False)
    pan_no = models.CharField(max_length=12,blank=False,null=False)
    dob = models.DateField(blank=False,null=False)
    image = models.FileField(blank=False,null=False,upload_to='upload/images')
    
    def __str__(self):
        return self.pan_no
    
class IssuedDoc(models.Model):
    category = models.CharField(max_length=10,blank=False,null=False)
    username = models.CharField(max_length=20,blank=False,null=False)
    firstname = models.CharField(max_length=50,blank=False,null=False)
    lastname = models.CharField(max_length=50,blank=False,null=False)
    gender = models.CharField(max_length=12,blank=False,null=False)
    card_no = models.CharField(max_length=12,blank=False,null=False)
    dob = models.CharField(max_length=10,blank=False,null=False)
    image = models.CharField(max_length=200,blank=False,null=False)
    
    def __str__(self):
        return self.category