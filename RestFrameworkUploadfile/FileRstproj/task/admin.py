from django.contrib import admin
from .models import UserFile,SingleUser


# Register your models here.
@admin.register(UserFile)
class UserFileAdmin(admin.ModelAdmin):
    list_display = ['user','photo','xlsdoc','idproof']

@admin.register(SingleUser)
class SingleUseradmin(admin.ModelAdmin):
    list_display = ['user','docfiles']