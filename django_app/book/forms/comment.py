from django import forms

from book.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'star_score',
            'content',
        )

    STAR_VALUE_1 = '⭐'
    STAR_VALUE_2 = '⭐⭐'
    STAR_VALUE_3 = '⭐⭐⭐'
    STAR_VALUE_4 = '⭐⭐⭐⭐'
    STAR_VALUE_5 = '⭐⭐⭐⭐⭐'

    STAR_VALUE_CHOICES = (
        (5, STAR_VALUE_5),
        (4, STAR_VALUE_4),
        (3, STAR_VALUE_3),
        (2, STAR_VALUE_2),
        (1, STAR_VALUE_1),
    )

    star_score = forms.ChoiceField(
        label='',
        choices=STAR_VALUE_CHOICES,
    )

    content = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'id': 'autocomplete',
                'class': 'textarea',
            }
        )
    )

