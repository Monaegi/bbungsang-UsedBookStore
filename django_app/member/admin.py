from django.contrib.auth import get_user_model
from django.contrib import admin

MyUser = get_user_model()


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'username', 'nickname', ]
