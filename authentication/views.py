from django.shortcuts import render, redirect

from django.contrib.auth import (
    login,
    logout,
    authenticate
)

from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm
)

def signin(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)
                return redirect('/')

    if request.user.is_authenticated:
        return redirect('/')

    return render(request, 'authentication/login.html', { 'form': form })

def signup(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            user = form.save()

            if user is not None:
                login(request, user)
                return redirect('/')

    if request.user.is_authenticated:
        return redirect('/')

    return render(request, 'authentication/register.html', { 'form': form })

def signout(request):
    logout(request)
    return redirect('/authentication/login')
