from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django_messages.forms import ComposeForm

from book.forms.book_register import SellBookRegisterForm
from book.forms.comment import CommentForm
from book.forms.searchs import NaverBooksSearchForm
from book.models import SellBookRegister, Book, BuyBookRegister, Comment

MyUser = get_user_model()


def sell_book_register(request, ):
    """ 팔려는 책 등록하기 """

    if request.method == 'POST':
        form = SellBookRegisterForm(data=request.POST)

        if form.is_valid():
            sell_book = form.save(seller=request.user.my_seller)
            sell_isbn = form.data.get('isbn')
            book_info = Book.objects.get(isbn=sell_isbn)

            if BuyBookRegister.objects.filter(book_info_id=book_info.pk):
                data = {
                    'recipient': request.user.username,
                    'subject': '안녕하세요!',
                    'body': '{}님이 판매하시려는 책의 구매 리스트에 존재합니다. 구매 리스트를 확인해보세요 :-)'.format(request.user.username),
                }
                compose_form = ComposeForm(data)
                sender = MyUser.objects.get(pk=1)

                if compose_form.is_valid():
                    compose_form.save(sender=sender)
                    return redirect('book:sell_book_detail', sell_pk=sell_book.pk)

            return redirect('book:sell_book_detail', sell_pk=sell_book.pk)

    register_form = SellBookRegisterForm()
    search_form = NaverBooksSearchForm()
    context = {
        'register_form': register_form,
        'search_form': search_form,
    }
    return render(request, 'book/sell_book_register.html', context)


def sell_book_list(request):
    """ 팔려는 책 목록 """

    all_books = SellBookRegister.objects.all()
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
    return render(request, 'book/sell_book_list.html', context)


def sell_book_detail(request, sell_pk):
    """ 팔려는 책 디테일 """

    sell_book = SellBookRegister.objects.get(pk=sell_pk)
    comments = Comment.objects.filter(sell_book=sell_book)
    context = {
        'book': sell_book,
        'comment_form': CommentForm(),
        'comments': comments,
    }
    return render(request, 'book/sell_book_detail.html', context)