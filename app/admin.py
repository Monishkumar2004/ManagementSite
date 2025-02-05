from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# the below class can be user to modify the details shown in the admin panel , like there is a user model which is shown as users in the admin panel , we have changed the list details which should be shown on the page.
class UserModel(UserAdmin):
    list_display = ['username', 'email', 'user_type']

# Register your models here.
admin.site.register(CustomUser, UserModel)