from django.urls import path
from .views import *

urlpatterns = [
    path('all/', UserAll, name='users/all'),
    path('mapped/', UserMapped, name='users/mapped'),
]
