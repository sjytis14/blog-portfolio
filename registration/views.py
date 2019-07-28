from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('/')
    return render(request, 'registration/signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'registration/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'registration/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        redirect('/')
    return render(request, 'registration/login.html')