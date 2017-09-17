from django import forms


class NaverBooksSearchForm(forms.Form):
    q = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'type': 'search',
                'placeholder': '등록하실 책을 검색하세요 :D',
                'id': 'q',
            }
        )
    )


class CommonBooksSearchForm(forms.Form):
    pass
