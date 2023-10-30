from django.contrib import admin

# Register your models here.
from .models import AboutData, UserData

admin.site.register(AboutData)
admin.site.register(UserData)
