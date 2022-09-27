from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from accounts.forms import UserForm
from vendor.forms import VendorForm
from .models import User, UserProfile


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
    return render(request, 'accounts/register_user.html', context)


def register_vendor(request):
    if request.method == 'POST':
        # store the data and create the user
        form = UserForm(request.POST)
        vendor_form = VendorForm(request.POST, request.FILES)
        if form.is_valid() and vendor_form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                            username=username, email=email, password=password)

            user.role = User.VENDOR
            user.save()
            vendor = vendor_form.save(commit=False)
            vendor.user = user
            user_profile = UserProfile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save()
            messages.success(request, 'Your account has been registered successfully! Please wait for the approval.')
            return redirect('register_vendor')

        else:
            print('Invalid Form')
            print(form.errors)
            print(vendor_form.errors)

    else:
        form = UserForm()
        vendor_form = VendorForm()
    context = {
        'form': form,
        'vendor_form': vendor_form
    }
    return render(request, 'accounts/register_vendor.html', context=context)
