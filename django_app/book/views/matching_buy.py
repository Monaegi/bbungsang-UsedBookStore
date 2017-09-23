from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from django_messages.forms import ComposeForm

from book.forms.book_register import BuyBookRegisterForm
from book.forms.searchs import NaverBooksSearchForm
from book.models import BuyBookRegister, SellBookRegister, Book

MyUser = get_user_model()


def buy_book_register(request, ):

    if request.method == 'POST':
        form = BuyBookRegisterForm(data=request.POST)

        if form.is_valid():
            form.save(buyer=request.user)

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

                    return HttpResponse('성공!')

    register_form = BuyBookRegisterForm()
    search_form = NaverBooksSearchForm()

    context = {
        'register_form': register_form,
        'search_form': search_form,
    }
    return render(request, 'book/buy_book_register.html', context)


def buy_book_list(request, ):
    books = BuyBookRegister.objects.all()

    context = {
        'books': books,
    }

    return render(request, 'book/buy_book_list.html', context)


def buy_book_detail(request, pk):
    book = BuyBookRegister.objects.get(pk=pk)

    context = {
        'book': book,
    }

    return render(request, 'book/buy_book_detail.html', context)