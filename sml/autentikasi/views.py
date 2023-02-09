
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def loginUser(request):
    context = {
        "page_title": "Halaman Login"
    }

    if request.method == "POST":
        username_fr = request.POST['username']
        password_fr = request.POST['password']
        userLogin = authenticate(request, username=username_fr, password=password_fr)

        if userLogin is not None:
            login(request, userLogin)
            print('logged')
            return redirect('limbah/index')
            
        else:
            print('not logged')
            return redirect('login')

    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('limbah/index')
        else:
            return render(request, 'login.html', context)


@login_required
def logoutUser(request):
    context = {
        'page_title': 'Logout Page'
    }

    if logout(request):
        redirect('limbah/index')
    return redirect('login')
