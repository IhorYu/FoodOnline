from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from accounts.forms import UserForm
from .models import User


def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = User.CUSTOMER
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Your account has been registered')
            return redirect('register_user')
        else:
            print(form.errors)

    else:
        form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/registerUser.html', context)
