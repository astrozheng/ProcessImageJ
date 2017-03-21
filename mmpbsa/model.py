from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pdie = models.CharField(max_length=20)
    saltconc = models.CharField(max_length=20,)
    ligand = models.CharField(max_length=20,)

    docfile = models.FileField()

    def __unicode__(self):
        return self.username
