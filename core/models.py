from django.db import models

# Create your models here.


class Work_Details(models.Model):
    title = models.CharField(max_length=300)
    company = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=300)
    start_date = models.CharField(max_length=300)
    end_date = models.CharField(max_length=300)
    current = models.CharField(max_length=300)
