from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    code = models.CharField(max_length=25)
    user = models.OneToOneField(User,on_delete=models.CASCADE)