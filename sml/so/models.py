from django.db import models

#Model Sub Unit Bisnis
class BisnisUnit(models.Model):
  kode_bu = models.CharField(max_length=20, null=False)
  nama_bu = models.TextField(max_length=150, null=False)
  inserted_at = models.DateTimeField()
  updated_at = models.DateTimeField()

  def __str__(self):
    return self.nama_bu

  class Meta:
    db_table = '"sc_mst"."bisnis_unit"'


#Model Departemen
class Departmen(models.Model):
  kode_bu = models.ForeignKey(BisnisUnit, on_delete=models.CASCADE)
  kode_dept = models.CharField(max_length=20, null=False)
  nama_dept = models.TextField(max_length=150, null=False)
  inserted_at = models.DateTimeField()
  updated_at = models.DateTimeField()

  def __str__(self):
    return self.nama_dept +'-'+self.kode_bu.nama_bu

  class Meta:
    db_table = '"sc_mst"."departmen"'

#Model Sub Departemen
class SubDepartmen(models.Model):
  kode_bu = models.ForeignKey(BisnisUnit, on_delete=models.CASCADE)
  kode_dept = models.ForeignKey(Departmen, on_delete=models.CASCADE)
  kode_subdept = models.CharField(max_length=20, null=False)
  nama_subdept = models.TextField(max_length=150, null=False)
  inserted_at = models.DateTimeField()
  updated_at = models.DateTimeField()

  def __str__(self):
    return self.nama_subdept

  class Meta:
    db_table = '"sc_mst"."sub_departmen"'


#Model Sub Unit Bisnis
class SubUnitBisnis(models.Model):
  kode_bu = models.ForeignKey(BisnisUnit, on_delete=models.CASCADE)
  kode_subbu = models.CharField(max_length=20, primary_key=True)
  nama_subbu = models.TextField(max_length=150, null=False)
  inserted_at = models.DateTimeField()
  updated_at = models.DateTimeField()

  def __str__(self):
    return self.nama_subbu

  class Meta:
    db_table = '"sc_mst"."subunit_bisnis"'

