from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import LogbookLimbah, GroupLimbah, SubGroupLimbah, SubUnitBisnis, TujuanPenyimpananLimbah, SumberLimbah, KategoriLimbah, BisnisUnit, SubDepartmen, Departmen
from django.db import connections


@login_required(login_url='/autentikasi/')
def index(request):
    username = request.user.username.upper()
    uuid = request.user.id

    result = LogbookLimbah.objects.select_related('kode_grplbh', 'kode_subgrplbh', 'kode_lbh', 'kode_sbrlbh', 'kode_subbu', 'kode_tplbh')

    context = {
        "page_title": "Halaman Limbah",
        "breadcrumb": "Limbah Masuk",
        "username": username,
        "logbook": result
    }
    
    return render(request, "transaksi/log_limbah.html", context)


@login_required(login_url='/autentikasi/')
def limbahMasuk(request):
    username = request.user.username.upper()
    uuid = request.user.id

    result = LogbookLimbah.objects.select_related('kode_grplbh', 'kode_subgrplbh', 'kode_lbh', 'kode_sbrlbh', 'kode_subbu', 'kode_tplbh')

    context = {
        "page_title": "Halaman Limbah",
        "breadcrumb": "Limbah Masuk",
        "username": username,
        "logbook": result
    }
    
    return render(request, "transaksi/log_limbah.html", context)


@login_required(login_url='/autentikasi/')
def limbahKeluar(request):
    username = request.user.username.upper()
    uuid = request.user.id

    result = LogbookLimbah.objects.select_related('kode_grplbh', 'kode_subgrplbh', 'kode_lbh', 'kode_sbrlbh', 'kode_subbu', 'kode_tplbh')

    context = {
        "page_title": "Halaman Limbah",
        "breadcrumb": "Limbah Keluar",
        "username": username,
        "logbook": result
    }
    
    return render(request, "transaksi/log_limbah.html", context)


@login_required(login_url='/autentikasi/')
def transferLimbah(request):
    username = request.user.username.upper()
    uuid = request.user.id

    # ambil data master
    idbu = BisnisUnit.objects.all()
    dept = Departmen.objects.all()
    subdept = SubDepartmen.objects.all()
    subbu = SubUnitBisnis.objects.all()
    group = GroupLimbah.objects.all()
    subgroup = SubGroupLimbah.objects.all()
    kat_limbah = KategoriLimbah.objects.all()
    sumber_limbah = SumberLimbah.objects.all()
    tp_limbah = TujuanPenyimpananLimbah.objects.all()

    context = {
        "page_title": "Halaman Transfer Limbah",
        "breadcrumb": "Transfer Limbah",
        "username": username,
        "idbu": idbu,
        "subdept": subdept,
        "subbu": subbu,
        "group": group,
        "subgroup": subgroup,
        "kat_limbah": kat_limbah,
        "sumber_limbah": sumber_limbah,
        "tp_limbah": tp_limbah,
    }
    
    return render(request, "transaksi/transfer_limbah.html", context)


@login_required(login_url='/autentikasi/')
def groupLimbah(request):
    username = request.user.username.upper()
    
    if request.user.is_authenticated:
        # Ambil data group limbah
        grp_limbah = GroupLimbah.objects.all()
        context = {
            "page_title": "Halaman Group Limbah",
            "breadcrumb": "Group Limbah",
            "group_limbah": grp_limbah,
            "username": username,
        }
        return render(request, "master/group_limbah.html", context)
    else:
        # jika anonymous
        return redirect('login')


@login_required(login_url='/autentikasi/')
def subGroupLimbah(request):
    username = request.user.username.upper()
    
    if request.user.is_authenticated:
        # Ambil data group limbah
        subgrp_limbah = SubGroupLimbah.objects.select_related('kode_grplbh')
        context = {
            "page_title": "Halaman Sub Group Limbah",
            "breadcrumb": "Sub Group Limbah",
            "subgroup_limbah": subgrp_limbah,
            "username": username,
        }
        return render(request, "master/subgroup_limbah.html", context)
    else:
        # jika anonymous
        return redirect('login')


@login_required(login_url='/autentikasi/')
def tujuanPenyimpananLimbah(request):
    username = request.user.username.upper()
    
    if request.user.is_authenticated:
        # Ambil data group limbah
        tjp_limbah = TujuanPenyimpananLimbah.objects.all()
        context = {
            "page_title": "Halaman Tujuan Penyimpanan Limbah",
            "breadcrumb": "Tujuan Penyimpanan Limbah",
            "tjp_limbah": tjp_limbah,
            "username": username,
        }
        return render(request, "master/tjp_limbah.html", context)
    else:
        # jika anonymous
        return redirect('login')


@login_required(login_url='/autentikasi/')
def kategoriLimbah(request):
    username = request.user.username.upper()
    
    if request.user.is_authenticated:
        # Ambil data kategori limbah
        kat_limbah = KategoriLimbah.objects.all()
        context = {
            "page_title": "Halaman Kategori Limbah",
            "breadcrumb": "Kategori Limbah",
            "kategori_limbah": kat_limbah,
            "username": username,
        }
        return render(request, "master/kategori_limbah.html", context)
    else:
        # jika anonymous
        return redirect('login')

@login_required(login_url='/autentikasi/')
def sumberLimbah(request):
    username = request.user.username.upper()
    if request.user.is_authenticated:
        # Ambil data kategori limbah
        smbr_limbah = SumberLimbah.objects.all()
        context = {
            "page_title": "Halaman Sumber Limbah",
            "breadcrumb": "Sumber Limbah",
            "sumber_limbah": smbr_limbah,
            "username": username,
        }
        return render(request, "master/sumber_limbah.html", context)
    else:
        # jika anonymous
        return redirect('login')
