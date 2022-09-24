from django.http import HttpResponse
from django.shortcuts import render, redirect

from accounts.forms import UserForm
from .models import User


def registerUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = User.CUSTOMER
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('registerUser')
        else:
            print(form.errors)

    else:
        form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/registerUser.html', context)


field = 1
feild =1


