from django.contrib import admin

from .models import Details,AadhaarDetails,PANdetails,IssuedDoc

# Register your models here.
admin.site.register(Details)
admin.site.register(AadhaarDetails)
admin.site.register(PANdetails)
admin.site.register(IssuedDoc)