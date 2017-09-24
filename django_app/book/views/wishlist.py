from django.http import HttpResponse

from book.models import SellBookRegister
from member.models import BookWishList


def book_wish_list(request, book_pk):
    book = SellBookRegister.objects.get(pk=book_pk)
    wish_lists = BookWishList.objects.filter(user=request.user)

    for wish_list in wish_lists:
        if book == wish_list.book:
            return HttpResponse('이미 위시리스트에 있는 상품입니다.')

    BookWishList.objects.create(
        user=request.user,
        book=book,
    )
    return HttpResponse('장바구니에 담기 성공!')