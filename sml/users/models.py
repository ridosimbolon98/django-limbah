from django.db import models
from django.conf import settings

#Model Mapping User Level
class MappingUser(models.Model):
  kd_mapuser = models.CharField(max_length=20, primary_key=True)
  uuid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=False)
  level = models.TextField(max_length=50, null=False)
  kd_dept = models.CharField(max_length=20, null=False) #kode departemen
  kd_bu = models.CharField(max_length=10, null=False) #kode bisnis unit
  status = models.BooleanField(default=True) #aktif dan tidak aktif
  inserted_at = models.DateTimeField()
  updated_at = models.DateTimeField()

  def __str__(self):
    return self.kd_mapuser+'-'+self.kd_dept+'-'+self.kd_bu+'-'+self.level

  class Meta:
    db_table = '"sc_mst"."mapping_user"'