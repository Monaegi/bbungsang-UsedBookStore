from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _


from book.models import Book, SellBookRegister

MyUser = get_user_model()


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'username', 'nickname', ]


class BookAdmin(admin.ModelAdmin):
    list_display = ['pk', 'get_book_image', 'title', 'author', 'publisher', 'category', ]

    def get_book_image(self, obj):
        image = obj.cover_img
        if not image:
            return ''
        return mark_safe('<img src={} width="80" height="110">'.format(image))
    get_book_image.short_description = _('책 이미지')

    list_per_page = 5


class SellBookRegisterAdmin(admin.ModelAdmin):
    list_display = ['pk', 'get_seller_username', 'get_book_title']

    def get_book_title(self, obj):
        return obj.book_info.title
    get_book_title.short_description = ('책 제목')

    def get_seller_username(self, obj):
        return obj.seller.user.username
    get_seller_username.short_description = _('판매자')


admin.site.unregister(MyUser, )
admin.site.register(Book, BookAdmin)
admin.site.register(SellBookRegister, SellBookRegisterAdmin)