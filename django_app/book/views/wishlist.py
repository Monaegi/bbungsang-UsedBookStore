from django.http import HttpResponse
from django.shortcuts import render, redirect

from book.models import SellBookRegister
from member.models import BookWishList


def book_wish_list(request, ):
    wish_lists = BookWishList.objects.filter(user=request.user)
    context = {
        'lists': wish_lists,
    }
    return render(request, 'wish/book_wish_list.html', context)


def book_wish_detail(request, book_pk):
    wish_lists = BookWishList.objects.filter(user=request.user)
    book = SellBookRegister.objects.get(pk=book_pk)

    if request.method == 'POST':

        for wish_list in wish_lists:
            if book == wish_list.book:
                return HttpResponse('이미 위시리스트에 있는 상품입니다.')

        BookWishList.objects.create(
            user=request.user,
            book=book,
        )
        return redirect('book:book_wish_list')

    context = {
        'book': book,
    }
    return render(request, 'wish/book_wish_detail.html', context)