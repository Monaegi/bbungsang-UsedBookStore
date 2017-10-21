from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django_messages.forms import ComposeForm

from book.forms import SellBookRegisterForm
from book.forms import CommentForm
from book.forms import NaverBooksSearchForm
from book.models import SellBookRegister, Book, BuyBookRegister, Comment, BookStatus
from member.models import News

MyUser = get_user_model()


def sell_book_register(request, ):
    """ 팔려는 책 등록하기 """

    if request.method == 'POST':
        files = request.FILES.getlist('sell_book_status')
        form = SellBookRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            sell_book = form.save(seller=request.user.my_seller)
            sell_isbn = form.data.get('isbn')
            book_info = Book.objects.get(isbn=sell_isbn)
            for f in files:
                BookStatus.objects.create(
                    sell_book_status=sell_book,
                    photo=f,
                )

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

            news = News.objects.filter(follow_other_id=request.user.id)
            if news:
                for other in news:
                    data = {
                        'recipient': other.my_follow.username,
                        'subject': '{}님께서 새로운 글을 등록했습니다.'.format(request.user.username, ),
                        'body': 'test',
                    }
                    compose_form = ComposeForm(data)
                    sender = request.user

                    if compose_form.is_valid():
                        compose_form.save(sender=sender)

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
    book_status = BookStatus.objects.filter(sell_book_status=sell_book)
    comments = Comment.objects.filter(sell_book=sell_book)
    context = {
        'book': sell_book,
        'book_status': book_status,
        'comment_form': CommentForm(),
        'comments': comments,
    }
    return render(request, 'book/sell_book_detail.html', context)