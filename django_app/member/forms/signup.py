from django import forms
from django.contrib.auth import get_user_model

MyUser = get_user_model()

__all__ = (
    "BasicInfoForm",
    "SignupForm"
)


class BasicInfoForm(forms.Form):

    nickname = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': '닉네임',
                'required': True
            }
        )
    )
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': '이메일',
                'required': True
            }
        )
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        nickname = self.cleaned_data.get('nickname')

        if MyUser.objects.filter(username=username) and MyUser.objects.filter(nickname=nickname):
            raise forms.ValidationError(
                '닉네임과 이메일이 모두 존재합니다. 다시 입력해주세요.'
            )
        elif MyUser.objects.filter(username=username):
            raise forms.ValidationError(
                '이메일이 이미 존재합니다. 다시 입력해주세요.'
            )
        elif MyUser.objects.filter(nickname=nickname):
            raise forms.ValidationError(
                '닉네임이 이미 존재합니다. 다시 입력해주세요.'
            )
        return self.cleaned_data


class SignupForm(forms.Form):
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '비밀번호',
                'required': True
            }
        )
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '비밀번호 확인',
                'required': True
            }
        )
    )
    phone = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': '핸드폰 번호',
            }
        )
    )

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError(
                '비밀번호가 서로 일치하지 않습니다.'
            )
        return self.cleaned_data