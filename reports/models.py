from django.db import models 
from django.contrib.auth.models import AbstractUser
# Create your models here.

class MyUser(AbstractUser):
    phone = models.TextField(name="Phone", max_length=25)
    USERNAME_FIELD = 'username'