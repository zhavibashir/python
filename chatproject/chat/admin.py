from django.contrib import admin
from .models import Message
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Message)
# admin.site.register(User, UserAdmin)
