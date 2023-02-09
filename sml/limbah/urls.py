from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='limbah/index'),
    path('masuk', limbahMasuk, name='limbah/masuk'),
    path('keluar', limbahKeluar, name='limbah/keluar'),
    path('transfer', transferLimbah, name='limbah/transfer'),
    path('kategori', kategoriLimbah, name='limbah/kategori'),
    path('sumber', sumberLimbah, name='limbah/sumber'),
    path('group', groupLimbah, name='limbah/group'), 
    path('subgroup', subGroupLimbah, name='limbah/subgroup'), 
    path('tujuan', tujuanPenyimpananLimbah, name='limbah/tujuan'), 
]


