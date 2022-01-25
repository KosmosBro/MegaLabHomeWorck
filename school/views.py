from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from school.forms import LoginForm, RegisterForm


def view_login(request):
    """ view входа в систему. """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
            else:
                form.add_error('login', 'Bad login or password')
                form.add_error('password', 'Bad login or password')
                return render(request, 'home.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'home.html', {'form': form})


def view_log_out(request):
    """ view выход пользователя из системы. """
    logout(request)
    return redirect('/')


def view_register(request):
    """ view регистрации пользователя. """
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.save()
            return redirect('/')
    else:
        user_form = RegisterForm()
    return render(request, 'register.html', {'user_form': user_form})
