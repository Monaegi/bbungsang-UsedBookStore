from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django_messages.forms import ComposeForm

from book.forms.book_register import BuyBookRegisterForm
from book.forms.searchs import NaverBooksSearchForm
from book.models import BuyBookRegister, SellBookRegister, Book

MyUser = get_user_model()


def buy_book_register(request, ):
    """ 사려는 책 등록하기 """

    if request.method == 'POST':
        form = BuyBookRegisterForm(data=request.POST)

        if form.is_valid():
            buy_book = form.save(buyer=request.user)
            buy_isbn = form.data.get('isbn')
            book_info = Book.objects.get(isbn=buy_isbn)

            if SellBookRegister.objects.filter(book_info_id=book_info.pk):
                data = {
                    'recipient': request.user.username,
                    'subject': '안녕하세요!',
                    'body': '{}님이 구매하시려는 책의 판매 리스트에 존재합니다. 판매 리스트를 확인해보세요 :-)'.format(request.user.username),
                }
                compose_form = ComposeForm(data)
                sender = MyUser.objects.get(pk=1)

                if compose_form.is_valid():
                    compose_form.save(sender=sender)
                    return redirect('book:buy_book_detail', buy_pk=buy_book.pk)

            return redirect('book:buy_book_detail', buy_pk=buy_book.pk)

    register_form = BuyBookRegisterForm()
    search_form = NaverBooksSearchForm()
    context = {
        'register_form': register_form,
        'search_form': search_form,
    }
    return render(request, 'book/buy_book_register.html', context)


def buy_book_list(request, ):
    """ 사려는 책 목록 """
    all_books = BuyBookRegister.objects.all()
    p = Paginator(all_books, 6)
    page_num = request.GET.get('page')

    try:
        books = p.page(page_num)
    except PageNotAnInteger:
        books = p.page(1)
    except EmptyPage:
        books = p.page(p.num_pages)

    context = {
        'all_books': all_books,
        'books': books,
    }

    return render(request, 'book/buy_book_list.html', context)


def buy_book_detail(request, buy_pk):
    """ 사려는 책 디테일 """

    buy_book = BuyBookRegister.objects.get(pk=buy_pk)
    context = {
        'book': buy_book,
    }
    return render(request, 'book/buy_book_detail.html', context)