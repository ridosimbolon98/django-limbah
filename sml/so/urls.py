from django.urls import path
from .views import *

urlpatterns = [
    path('bu/', DataBU, name='so/bu'),
    path('sbu/', SBU, name='so/sbu'),
    path('getsbu/', getSBU, name='so/getsbu'),
    path('dept/', DeptAll, name='so/dept'),
    path('subdept/', SubDept, name='so/subdept'),
]
