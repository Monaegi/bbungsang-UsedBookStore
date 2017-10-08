from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from book.models import SellBookRegister
from member.models import BookWishList


def book_wish_list(request, ):
    """ 위시리스트 """

    all_wish_lists = BookWishList.objects.filter(user=request.user)
    p = Paginator(all_wish_lists, 4)
    page_num = request.GET.get('page')

    try:
        wish_lists = p.page(page_num)
    except PageNotAnInteger:
        wish_lists = p.page(1)
    except EmptyPage:
        wish_lists = p.page(p.num_pages)

    context = {
        'all_wish_lists': all_wish_lists,
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
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = {
        'book': book,
    }
    return render(request, 'wish/book_wish_detail.html', context)