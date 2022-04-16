from datetime import datetime
from typing import Type
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class products(models.Model):
    name = models.TextField(max_length=150)
    description = models.TextField(max_length=1024, default='SOME STRING')

    def __str__(self):
        return self.name
    
class productmove(models.Model):
    product = models.ForeignKey(products, on_delete=models.RESTRICT)
    quantity = models.IntegerField()
    date = models.DateTimeField()
    
    def __str__(self):
        return "Move by " + str(self.date) 
    
class order(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    product = models.ForeignKey(products, on_delete=models.RESTRICT)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "Order of " + str(self.user) + " by " + str(self.date)
