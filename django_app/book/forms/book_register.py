from django import forms
from django.contrib.auth import get_user_model

from book.models import Book, BuyBookRegister

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

            # 'used_price',
            # 'etc_requirements',
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
        widget=forms.TextInput(
            attrs={
                'id': 'isbn',
                'readonly': 'readonly',
            }
        ),
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

        book_info, book_info_bool = Book.objects.get_or_create(
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
        instance.save()

        return instance


class SellBookRegisterForm(forms.Form):
    pass