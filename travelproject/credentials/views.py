from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST.get('email', 'None')
        password = request.POST.get('password', '')
        cpassword = request.POST.get('password1')

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already in use')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                # print('user crated')
                return redirect('login')
        messages.info(request, 'password not matched')
        return redirect('register')
        
    return render(request, 'register.html')

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    return render(request, 'login.html')

def userlogout(request):
    logout(request)
    return redirect('/')
