from django.shortcuts import render

from book.models import SellBookRegister


def main(request, ):

    new_books = SellBookRegister.objects.all()
    bonobono = SellBookRegister.objects.get(used_price='7000')
    context = {
        'new_books': new_books,
        'bonobono': bonobono,
    }
    return render(request, 'common/main.html', context)