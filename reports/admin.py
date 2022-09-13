from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser


# Register your models here.

class MyUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff'
    )


admin.site.register(MyUser, MyUserAdmin)
