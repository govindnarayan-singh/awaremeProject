from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class OrgDetail(models.Model):
    user=models.OneToOneField(User,null=True,blank=True, on_delete=models.CASCADE)
    mission=models.TextField(blank=True,null=True)
    Contact=models.CharField(max_length=15,null=True)
    portfolio=models.URLField(blank=True,null=True)
    # profile_pic=models.ImageField(upload_to='awareme\static\images',default='default.png',null=True)
    
    def __str__(self):
        return str(self.user)

class OrgFeed(models.Model):

    title=models.CharField(blank=True,null=True,max_length=250)
    brief=models.TextField(blank=True,null=True)
    author=models.CharField(blank=True,null=True,max_length=250)
    locations=models.CharField(max_length=100,null=True)
    timestamp = models.DateTimeField(default=now)
    def __str__(self):
        return self.title + ' by ' + self.author
    

class FeedComment(models.Model):
    comment=models.TextField(blank=True,null=True)
    writer=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(OrgFeed, on_delete=models.CASCADE)
    parent=models.ForeignKey('self', on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.writer) +' --wrote--> ' +self.comment[0:4] + '...'
    





