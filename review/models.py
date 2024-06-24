from django.db import models
class review(models.Model):
    name=models.CharField(max_length=50)
    rating=models.CharField(max_length=50)
    message=models.TextField()
# Create your models here.
