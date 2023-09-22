from django.shortcuts import render

from .models import User

# Create your views here.

def user_list():
    my_users = User.objects.all()
    
    context = {'my_users': my_users}
    
    return render()