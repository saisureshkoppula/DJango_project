from django.db import models

# Create your models here.

class student(models.Model):
    roll_number = models.IntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    mail_id = models.CharField(max_length=30)