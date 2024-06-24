from django.db import models
class pickup(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=50)
    address=models.TextField()
    scrap_type=models.CharField(max_length=50)
    date=models.DateField()
    time=models.TimeField()
    # Create your models here.
