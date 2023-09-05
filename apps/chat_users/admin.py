from django.contrib import admin
from apps.chat_users.models import User
from django.contrib.auth.admin import UserAdmin

#Register your models here.

class CustomUser(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
            ('Extra Fields', {'fields': ('title','bio')}),
)
    

admin.site.register(User, CustomUser)