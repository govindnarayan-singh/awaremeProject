from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class OrgDetail(models.Model):
    user=models.OneToOneField(User,null=True,blank=True, on_delete=models.CASCADE)
    mission=models.TextField(blank=True,null=True)
    Contact=models.CharField(max_length=15,null=True)
    portfolio=models.URLField(blank=True,null=True)
    profile_pic=models.ImageField(upload_to='awareme\static\images',default='default.png',null=True)
    
    def __str__(self):
        return str(self.user)

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
    timestamp = models.DateTimeField(default=now)
    def __str__(self):
        return self.title + ' by ' + self.author
    

class FeedComment(models.Model):
    comment=models.TextField(blank=True,null=True)
    writer=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(OrgFeed, on_delete=models.CASCADE)
    parent=models.ForeignKey('self', on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(default=now)





