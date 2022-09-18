from django.db import models

# Create your models here.
class Contact(models.Model):
    email=models.CharField(max_length=122,null=True,blank=True)
    name=models.CharField(max_length=122,null=True,blank=True)
    ct=models.CharField(max_length=122,null=True,blank=True)
    num=models.CharField(max_length=122,null=True,blank=True)
    #desc=models.CharField(max_length=122,null=True)
    #date=models.DateField()
    
    def __str__(self):
        return self.name