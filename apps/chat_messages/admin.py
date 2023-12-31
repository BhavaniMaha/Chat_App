from django.contrib import admin
from apps.chat_messages import models

# Register your models here.

class MessageDetails(admin.ModelAdmin):
    list_display = (
        "sending_user",
        "receiving_user",
    )
    




admin.site.register(models.Message, MessageDetails)
admin.site.register(models.Category)