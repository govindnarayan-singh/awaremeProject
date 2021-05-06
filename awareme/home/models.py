from django.db import models
from django.utils.timezone import now

class Contact(models.Model):
    srno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    phone=models.CharField(max_length=20,null=True)
    content=models.TextField()
    timestamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.name + ' - ' + self.email
    

