from django.urls import path
from .views import *

urlpatterns = [
    path('', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
]
