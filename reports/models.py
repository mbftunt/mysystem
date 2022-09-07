from django.db import models 
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
# Create your models here.

class MyUser(AbstractUser):
    phone = models.TextField(name="Phone", max_length=25)
    USERNAME_FIELD = 'username'