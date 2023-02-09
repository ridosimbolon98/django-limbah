from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import SubUnitBisnis, BisnisUnit, SubDepartmen
from django.http import HttpRequest, JsonResponse
import json

# Ambil Data Bisnis Unit All
@login_required(login_url='/autentikasi/')
def DataBU(request):
    context = {
        "page_title": "Home Page",
    }
    return render(request, "home.html", context)

# Ambil Data Sub Unit
@login_required(login_url='/autentikasi/')
def SBU(request):
    context = {
        "page_title": "Home Page",
    }
    return render(request, "home.html", context)

# Ambil Data Departemen All
@login_required(login_url='/autentikasi/')
def DeptAll(request):
    context = {
        "page_title": "Home Page",
    }
    return render(request, "home.html", context)

# Ambil Data Sub Departemen
@login_required(login_url='/autentikasi/')
def SubDept(request):
    context = {
        "page_title": "Home Page",
    }
    return render(request, "home.html", context)


# Ambil Data Get Sub BU
@login_required(login_url='/autentikasi/')
def getSBU(request: HttpRequest):
    kdbu = request.POST['data_bu']
    bu = BisnisUnit.objects.filter(kode_bu=kdbu)
    sdept = SubDepartmen.objects.filter(kode_bu_id=bu[0].id)
    sub = SubUnitBisnis.objects.filter(kode_bu_id=bu[0].id)
    data_subbu = []
    data_dept = []
    for i in sub:
        data_subbu.append({"kode_subbu": i.pk,"nama_subbu": i.nama_subbu})
    for d in sdept:
        data_dept.append({"kode_subdept": d.pk,"nama_subdept": d.nama_subdept})
    data = [data_subbu,data_dept]
    return JsonResponse(data, safe=False)
