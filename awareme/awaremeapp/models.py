from django.db import models
from phone_field import PhoneField
# from django.contrib.auth.models import User



class OrgModel(models.Model):
    name=models.CharField(blank=True,null=True,max_length=250)
    mission=models.TextField(blank=True,null=True)
    Contact=PhoneField(blank=True,help_text='Contact phone number')
    portfolio=models.URLField(blank=True,null=True)
    
    def __str__(self):
        return self.name
    




