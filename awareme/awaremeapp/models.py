from django.db import models
from phone_field import PhoneField
# from django.contrib.auth.models import User



class OrgDetail(models.Model):
    name=models.CharField(blank=True,null=True,max_length=250)
    mission=models.TextField(blank=True,null=True)
    Contact=PhoneField(blank=True,help_text='Contact phone number')
    portfolio=models.URLField(blank=True,null=True)
    
    def __str__(self):
        return self.name

class OrgFeed(models.Model):


    statesNunions=[('Andhra Pradesh','Andhra Pradesh'),('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),('Bihar','Bihar'),('Chhattisgarh','Chhattisgarh'),('Goa','Goa'),
    ('Gujarat','Gujarat'),('Haryana','Haryana'),('Himachal Pradesh','Himachal Pradesh'),
    ('Jharkhand','Jharkhand'),('Karnataka','Karnataka'),('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),('Maharashtra','Maharashtra'),('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),('Mizoram','Mizoram'),('Nagaland','Nagaland'),('Odisha','Odisha'),
    ('Punjab','Punjab'),('Rajasthan','Rajasthan'),('Sikkim','Sikkim'),('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),('Tripura','Tripura'),('Uttar Pradesh','Uttar Pradesh'),
    ('Uttarakhand','Uttarakhand'),('West Bengal','West Bengal'),('Andaman Nicobar Islands','Andaman Nicobar Islands'),
    ('Chandigarh','Chandigarh'),('Dadra Nagar Haveli and Daman Diu','Dadra Nagar Haveli and Daman Diu'),
    ('Delhi','Delhi'),('Jammu and Kashmir','Jammu and Kashmir'),('Lakshadweep','Lakshadweep'),
    ('Puducherry','Puducherry'),('Ladakh','Ladakh')]


    title=models.CharField(blank=True,null=True,max_length=250)
    brief=models.TextField(blank=True,null=True)
    author=models.CharField(blank=True,null=True,max_length=250)
    locations=models.CharField(choices=statesNunions,max_length=100)
    address=models.CharField(blank=True,null=True,max_length=500)
    start_datetime = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
    





