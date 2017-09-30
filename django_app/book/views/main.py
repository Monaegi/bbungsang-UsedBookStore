from django.shortcuts import render

from book.models import SellBookRegister


def main(request, ):

    new_books = SellBookRegister.objects.all()

    context = {
        'new_books': new_books,
    }
    return render(request, 'common/main.html', context)