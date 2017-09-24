from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout

from member.forms.login import LoginForm


def login(request, ):
    form = LoginForm(data=request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = form.cleaned_data['user']
            django_login(request, user)
            return redirect('book:main')
    else:
        if request.user.is_authenticated():
            return redirect('book:main')
        form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'member/login.html', context)

