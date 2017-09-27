from django.shortcuts import redirect

from book.forms.comment import CommentForm
from book.models import SellBookRegister


def create_comment(request, sell_pk):
    form = CommentForm(request.POST)
    sell_book = SellBookRegister.objects.get(pk=sell_pk)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.sell_book = sell_book
        comment.save()

        return redirect('book:sell_book_detail', sell_pk=sell_pk)