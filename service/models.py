from django.db import models
class service(models.Model):
    name=models.CharField(max_length=50)
    e_mail=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=10)
    subject=models.CharField(max_length=50)
    message=models.TextField()
# Create your models here.
