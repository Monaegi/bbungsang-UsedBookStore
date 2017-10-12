from django import forms
from django.contrib.auth import get_user_model

from book.models import Book, BuyBookRegister, SellBookRegister

MyUser = get_user_model()


class BuyBookRegisterForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = [
            'cover_img',
            'title',
            'author',
            'publisher',
            'normal_price',
            'publication_date',
            'isbn',
            'category',
        ]

    cover_img = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'id': 'cover_img',
                'readonly': 'readonly',
            }
        ),
    )

    title = forms.CharField(
        label='책 제목',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'id': 'title',
                'readonly': 'readonly',
                'value': '',
            }
        ),
    )

    author = forms.CharField(
        label='저자',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'id': 'author',
                'readonly': 'readonly',
            }
        ),
    )

    publisher = forms.CharField(
        label='출판사',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'id': 'publisher',
                'readonly': 'readonly',
            }
        )
    )

    normal_price = forms.CharField(
        label='정상가',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'id': 'normal_price',
                'readonly': 'readonly',
            }
        ),
    )

    publication_date = forms.CharField(
        label='발행일',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'id': 'publication_date',
                'readonly': 'readonly',
            }
        ),
    )

    isbn = forms.CharField(
        label_suffix='',
        label='ISBN',
        widget=forms.TextInput(
            attrs={
                'id': 'isbn',
                'readonly': 'readonly',
            }
        ),
    )

    BOOK_TYPE_LANG = '프로그래밍언어'
    BOOK_TYPE_OS = '운영체제'
    BOOK_TYPE_ALGORITHM = '자료구조/알고리즘'
    BOOK_TYPE_NETWORK = '네트워크'
    BOOK_TYPE_DB = '데이터베이스'
    BOOK_TYPE_ETC = 'ETC'

    BOOK_TYPE_CHOICES = (
        (BOOK_TYPE_LANG, '언어'),
        (BOOK_TYPE_OS, '운영체제'),
        (BOOK_TYPE_ALGORITHM, '자료구조/알고리즘'),
        (BOOK_TYPE_NETWORK, '네트워크'),
        (BOOK_TYPE_DB, '데이터베이스'),
        (BOOK_TYPE_ETC, 'etc(소프트웨어공학 등)'),
    )

    category = forms.ChoiceField(
        label_suffix='',
        label='카테고리',
        choices=BOOK_TYPE_CHOICES,
    )

    used_price = forms.CharField(
        label_suffix='',
        label='중고가',
        widget=forms.TextInput(
            attrs={
                'id': 'used-price',
                'class': 'used-price',
            }
        ),
    )

    etc_requirements = forms.CharField(
        label_suffix='',
        label='기타 요구사항',
        widget=forms.TextInput(
            attrs={
                'id': 'etc',
                'class': 'etc'
            }
        ),
    )

    def save(self, **kwargs):

        cover_img = self.cleaned_data.get('cover_img', '')
        title = self.cleaned_data.get('title', '')
        author = self.cleaned_data.get('author', '')
        publisher = self.cleaned_data.get('publisher', '')
        normal_price = self.cleaned_data.get('normal_price', '')
        publication_date = self.cleaned_data.get('publication_date', '')
        isbn = self.cleaned_data.get('isbn', '')
        category = self.cleaned_data.get('category', '')
        used_price = self.cleaned_data.get('used_price', '')
        etc_requirements = self.cleaned_data.get('etc_requirements', '')

        buyer = kwargs.pop('buyer', None)

        if Book.objects.filter(isbn=isbn):
            book_info = Book.objects.get(isbn=isbn)
        else:
            book_info = Book.objects.create(
                cover_img=cover_img,
                title=title,
                author=author,
                publisher=publisher,
                normal_price=normal_price,
                publication_date=publication_date,
                isbn=isbn,
                category=category,
            )

        instance = BuyBookRegister.objects.create(
            buyer=buyer,
            book_info=book_info,
            used_price=used_price,
            etc_requirements=etc_requirements

        )

        return instance


class SellBookRegisterForm(forms.Form):

    class Meta:
        model = Book
        fields = [
            'cover_img',
            'title',
            'author',
            'publisher',
            'normal_price',
            'publication_date',
            'isbn',
            'category',

            # 'used_price',
            # 'book_status',
        ]

    cover_img = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'id': 'cover_img',
                'readonly': 'readonly',
            }
        ),
    )

    title = forms.CharField(
        label='책 제목',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'id': 'title',
                'readonly': 'readonly',
            }
        ),
    )

    author = forms.CharField(
        label='저자',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'id': 'author',
                'readonly': 'readonly',
            }
        ),
    )

    publisher = forms.CharField(
        label='출판사',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'id': 'publisher',
                'readonly': 'readonly',
            }
        )
    )

    normal_price = forms.CharField(
        label='정상가',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'id': 'normal_price',
                'readonly': 'readonly',
            }
        ),
    )

    publication_date = forms.CharField(
        label='발행일',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'id': 'publication_date',
                'readonly': 'readonly',
            }
        ),
    )

    isbn = forms.CharField(
        label_suffix='',
        label='ISBN',
        widget=forms.TextInput(
            attrs={
                'id': 'isbn',
                'readonly': 'readonly',
            }
        ),
    )

    BOOK_TYPE_LANG = '프로그래밍언어'
    BOOK_TYPE_OS = '운영체제'
    BOOK_TYPE_ALGORITHM = '자료구조/알고리즘'
    BOOK_TYPE_NETWORK = '네트워크'
    BOOK_TYPE_DB = '데이터베이스'
    BOOK_TYPE_ETC = 'ETC'

    BOOK_TYPE_CHOICES = (
        (BOOK_TYPE_LANG, '언어'),
        (BOOK_TYPE_OS, '운영체제'),
        (BOOK_TYPE_ALGORITHM, '자료구조/알고리즘'),
        (BOOK_TYPE_NETWORK, '네트워크'),
        (BOOK_TYPE_DB, '데이터베이스'),
        (BOOK_TYPE_ETC, 'etc(소프트웨어공학 등)'),
    )

    category = forms.ChoiceField(
        label_suffix='',
        label='카테고리',
        choices=BOOK_TYPE_CHOICES,
    )

    used_price = forms.CharField(
        label_suffix='',
        label='중고가',
        widget=forms.TextInput(
            attrs={
                'id': 'used-price',
                'class': 'used-price',
            }
        ),
    )

    # book_status1 = forms.ImageField(
    #     label_suffix='',
    #     label='책 상태',
    #     widget=forms.FileInput(
    #         attrs={
    #             'id': 'book_status1',
    #             'class': 'book_status1'
    #         }
    #     ),
    # )
    #
    # book_status2 = forms.ImageField(
    #     required=False,
    #     label_suffix='',
    #     label='책 상태',
    #     widget=forms.FileInput(
    #         attrs={
    #             'id': 'book_status2',
    #             'class': 'book_status2'
    #         }
    #     ),
    # )
    #
    # book_status3 = forms.ImageField(
    #     required=False,
    #     label_suffix='',
    #     label='책 상태',
    #     widget=forms.FileInput(
    #         attrs={
    #             'id': 'book_status3',
    #             'class': 'book_status3'
    #         }
    #     ),
    # )

    def save(self, **kwargs):

        cover_img = self.cleaned_data.get('cover_img', '')
        title = self.cleaned_data.get('title', '')
        author = self.cleaned_data.get('author', '')
        publisher = self.cleaned_data.get('publisher', '')
        normal_price = self.cleaned_data.get('normal_price', '')
        publication_date = self.cleaned_data.get('publication_date', '')
        isbn = self.cleaned_data.get('isbn', '')
        category = self.cleaned_data.get('category', '')
        used_price = self.cleaned_data.get('used_price', '')
        # book_status1 = self.cleaned_data.get('book_status1', '')
        # book_status2 = self.cleaned_data.get('book_status2', '')
        # book_status3 = self.cleaned_data.get('book_status3', '')

        seller = kwargs.pop('seller', None)

        if Book.objects.filter(isbn=isbn):
            book_info = Book.objects.get(isbn=isbn)
        else:
            book_info = Book.objects.create(
                cover_img=cover_img,
                title=title,
                author=author,
                publisher=publisher,
                normal_price=normal_price,
                publication_date=publication_date,
                isbn=isbn,
                category=category,
            )

        instance = SellBookRegister.objects.create(
            seller=seller,
            book_info=book_info,
            used_price=used_price,
            # book_status1=book_status1,
            # book_status2=book_status2,
            # book_status3=book_status3,
        )

        return instance