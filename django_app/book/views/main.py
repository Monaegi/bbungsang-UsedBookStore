from django.shortcuts import render

from book.models import SellBookRegister


def main(request, ):

    new_books = SellBookRegister.objects.all()
    bonobono = SellBookRegister.objects.get(pk=1)
    context = {
        'new_books': new_books,
        'bonobono': bonobono,
    }
    return render(request, 'common/main.html', context)