import datetime
from time import time
from django.db import models
        
class student(models.Model):
        name = models.CharField(max_length=100)
        roll_number=models.IntegerField()
        gender_choice =(
            ('male','male'),
            ('female','female')
        )
        gender=models.CharField(max_length=10,choices=gender_choice)
        email = models.EmailField(max_length=50)
        phone =models.IntegerField()
        branch=models.CharField(max_length=50)
        sem = models.CharField(max_length=50)
        subject = models.CharField(max_length=70)
        present = models.BooleanField(default=False)
        image= models.ImageField(upload_to="media/")
        updated = models.DateTimeField(auto_now=True)
        shift = models.TimeField()
        
class Lastface(models.Model):
        last_face = models.CharField(max_length=200)
        date = models.DateTimeField(auto_now_add=True)      
        
        

# Create your models here.
