from django.db import models
from apps.core.models import CreatedModifiedDateTimeBase

#from django.contrib.auth.models import AbstractUser

#Create your models here.

class Message(CreatedModifiedDateTimeBase):
    # id=None # If you don't want the default id to be created
    #username = models.CharField(max_length=50)
    sending_user = models.ForeignKey('chat_users.User', on_delete=models.CASCADE, related_name='sending_user')
    receiving_user = models.ForeignKey('chat_users.User', on_delete=models.CASCADE, related_name='receiving_user')
    message_body = models.TextField()
    
    class Meta:
        verbose_name_plural = "Message"

    def __str__(self):
        return f'from {self.sending_user.username} to {self.receiving_user.username}'


class Category(CreatedModifiedDateTimeBase):
    cat = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.cat
    
    