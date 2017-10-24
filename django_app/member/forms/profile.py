from django import forms
from django.contrib.auth import get_user_model

MyUser = get_user_model()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'nickname', 'my_photo', 'phone']