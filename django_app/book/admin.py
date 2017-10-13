from django.contrib import admin
from django.contrib.auth import get_user_model

from book.models import Book, SellBookRegister

MyUser = get_user_model()


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'nickname', ]


class BookAdmin(admin.ModelAdmin):
    pass


class SellBookRegisterAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)
admin.site.register(SellBookRegister, SellBookRegisterAdmin)