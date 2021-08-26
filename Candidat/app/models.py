from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Taburl(models.Model):
    basic = models.CharField(max_length=250)
    miniurl = models.CharField(max_length=9)
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    nb = models.IntegerField(default=0)