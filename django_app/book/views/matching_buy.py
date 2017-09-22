from django.http import HttpResponse
from django.shortcuts import render

from book.forms.book_register import BuyBookRegisterForm
from book.forms.searchs import NaverBooksSearchForm
from book.models import BuyBookRegister


def buy_book_register(request, ):

    if request.method == 'POST':
        form = BuyBookRegisterForm(data=request.POST)

        if form.is_valid():
            form.save(buyer=request.user)

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