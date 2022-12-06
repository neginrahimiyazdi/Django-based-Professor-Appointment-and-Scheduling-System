from imaplib import _Authenticator
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('emial')
            #username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate( email, password)
            login(request,user)

            messages.success(request, f'Account created for {email}!')
            return redirect('user_timeline')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
