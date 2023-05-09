from django.contrib import admin
from .models import CustomUser
from rest_framework.authtoken.models import Token
# Register your models here.

admin.site.register(CustomUser)