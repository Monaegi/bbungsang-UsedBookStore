from django.http import HttpResponse
from django.shortcuts import render

from book.forms.book_register import SellBookRegisterForm
from book.forms.searchs import NaverBooksSearchForm
from book.models import SellBookRegister


def sell_book_register(request, ):

    if request.method == 'POST':
        form = SellBookRegisterForm(data=request.POST)

        if form.is_valid():
            form.save(seller=request.user.my_seller)

            return HttpResponse('성공!')

    register_form = SellBookRegisterForm()
    search_form = NaverBooksSearchForm()

    context = {
        'register_form': register_form,
        'search_form': search_form,
    }
    return render(request, 'book/sell_book_register.html', context)


def sell_book_list(request, ):
    books = SellBookRegister.objects.all()

    context = {
        'books': books,
    }

    return render(request, 'book/sell_book_list.html', context)


def sell_book_detail(request, pk):
    book = SellBookRegister.objects.get(pk=pk)

    context = {
        'book': book,
    }

    return render(request, 'book/sell_book_detail.html', context)