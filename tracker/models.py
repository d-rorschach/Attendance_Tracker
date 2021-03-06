from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class subject(models.Model):
    sub_name=models.CharField(max_length=50)
    prof=models.CharField(max_length=50,default="na")
    sunday=models.BooleanField(default=False)
    monday=models.BooleanField(default=False)
    tuesday=models.BooleanField(default=False)
    wednesday=models.BooleanField(default=False)
    thursday=models.BooleanField(default=False)
    friday=models.BooleanField(default=False)
    saturday=models.BooleanField(default=False)
    total_class=models.IntegerField(default=0)
    present=models.IntegerField(default=0)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.sub_name


class attend(models.Model):
    date=models.CharField(max_length=50)
    listed_subjects= models.ManyToManyField(subject)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.date)

