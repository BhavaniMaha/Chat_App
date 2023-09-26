from django.db import models
from apps.core.models import CreatedModifiedDateTimeBase

#from django.contrib.auth.models import AbstractUser

#Create your models here.

class Message(CreatedModifiedDateTimeBase):
    # id=None # If you don't want the default id to be created
    username = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "Message"

    def __str__(self):
        return self.username


class Category(CreatedModifiedDateTimeBase):
    cat = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.cat
    
    