from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Ambil Data User All
@login_required(login_url='/autentikasi/')
def UserAll(request):
    context = {
        "page_title": "Home Page",
    }
    return render(request, "home.html", context)

# Ambil Data User Mapped
@login_required(login_url='/autentikasi/')
def UserMapped(request):
    context = {
        "page_title": "Home Page",
    }
    return render(request, "home.html", context)