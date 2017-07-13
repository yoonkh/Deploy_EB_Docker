from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model


class MyUser(AbstractUser):
    img_profile = models.ImageField(upload_to='user', blank=True)

