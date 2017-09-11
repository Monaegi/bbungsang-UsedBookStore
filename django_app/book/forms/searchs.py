from django import forms


class NaverBooksSearchForm(forms.Form):
    q = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'type': 'search',
                'placeholder': 'Search...',
                'class': 'naver_books_search',
                'id': 'q',
            }
        )
    )


class CommonBooksSearchForm(forms.Form):
    pass
