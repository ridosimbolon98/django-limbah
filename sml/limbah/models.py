from django.db import models
from django.conf import settings
from so.models import *

#===============================================================================
#===============================================================================

#Model Kategori Limbah
class KategoriLimbah(models.Model):
  kode_lbh = models.CharField(max_length=20, primary_key=True)
  nama_lbh = models.CharField(max_length=50, null=False)
  desk_lbh = models.TextField(max_length=150, null=False)
  enabled = models.BooleanField(default=True)
  inserted_at = models.DateTimeField()
  updated_at = models.DateTimeField()

  def __str__(self):
    return self.nama_lbh

  class Meta:
    db_table = '"sc_mst"."kategori_limbah"'


#Model Group Limbah
class GroupLimbah(models.Model):
  kode_grplbh = models.CharField(max_length=20, primary_key=True)
  nama_grplbh = models.CharField(max_length=50, null=False)
  desk_grplbh = models.TextField(max_length=150, null=False)
  inserted_at = models.DateTimeField()
  updated_at = models.DateTimeField()

  def __str__(self):
    return self.nama_grplbh

  class Meta:
    db_table = '"sc_mst"."group_limbah"'


#Model Sub Group Limbah
class SubGroupLimbah(models.Model):
  kode_subgrplbh = models.CharField(max_length=20, primary_key=True)
  kode_grplbh = models.ForeignKey(GroupLimbah, on_delete=models.CASCADE) #kode group limbah
  nama_subgrplbh = models.CharField(max_length=50, null=False)
  desk_subgrplbh = models.TextField(max_length=150, null=False)
  inserted_at = models.DateTimeField()
  updated_at = models.DateTimeField()

  def __str__(self):
    return self.nama_subgrplbh

  class Meta:
    db_table = '"sc_mst"."subgroup_limbah"'


#Model Sumber Limbah
class SumberLimbah(models.Model):
  kode_sbrlbh = models.CharField(max_length=20, primary_key=True)
  desk_sbrlbh = models.TextField(max_length=150, null=False)
  inserted_at = models.DateTimeField()
  updated_at = models.DateTimeField()

  def __str__(self):
    return self.desk_sbrlbh

  class Meta:
    db_table = '"sc_mst"."sumber_limbah"'


#Model Tujuan Penyimpanan Limbah
class TujuanPenyimpananLimbah(models.Model):
  kode_tplbh = models.CharField(max_length=20, primary_key=True)
  desk_tplbh = models.TextField(max_length=150, null=False)
  inserted_at = models.DateTimeField()
  updated_at = models.DateTimeField()

  def __str__(self):
    return self.desk_tplbh

  class Meta:
    db_table = '"sc_mst"."tujuan_limbah"'


#Model Logbook Limbah
class LogbookLimbah(models.Model):
  no_dokumen = models.CharField(max_length=20, primary_key=True)
  kode_bu = models.TextField(max_length=150, null=False) #kode bisnis unit
  kode_subbu = models.ForeignKey(SubUnitBisnis, on_delete=models.CASCADE) #kode sub unit bisnis
  kode_grplbh = models.ForeignKey(GroupLimbah, on_delete=models.CASCADE) #kode group limbah
  kode_subgrplbh = models.ForeignKey(SubGroupLimbah, on_delete=models.CASCADE) #kode sub group limbah
  kode_lbh = models.ForeignKey(KategoriLimbah, on_delete=models.CASCADE) #kode kategori limbah
  kode_subdept = models.CharField(max_length=20, null=False) #kode sub departemen
  kode_sbrlbh = models.ForeignKey(SumberLimbah, on_delete=models.CASCADE) #kode umber limbah
  tipe_trx = models.CharField(choices=(
                    ('IN', "MASUK"),
                    ('OUT', "KELUAR"),
                ), max_length=4) #tipe transaksi limbah
  tgl_lbh = models.DateField() #tgl limbah
  tgl_max_lbh = models.DateField() #tgl maksimal penyimpanan limbah
  qty_lbh = models.FloatField(null=False) #kuantitas limbah
  kode_tplbh = models.ForeignKey(TujuanPenyimpananLimbah, on_delete=models.CASCADE) #kode tujuan penyimpanan limbah
  evidence = models.TextField(max_length=250, null=True) #evidence nomor dokumen rujukan
  deksripsi = models.TextField(max_length=250, null=True) #deskripsi atau penjelasan
  status = models.CharField(choices=(
                    ('I', "MASUK"),
                    ('P', "TERKIRIM"),
                ), max_length=4) #status notifikasi
  input_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=False)
  inserted_at = models.DateTimeField()
  updated_at = models.DateTimeField()

  def __str__(self):
    return self.no_dokumen +'-'+ self.tipe_trx

  class Meta:
    db_table = '"sc_trx"."logbook_limbah"'