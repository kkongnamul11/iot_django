from django.urls import path, include
from .views import *

urlpatterns = [
    path('input/<str:humi>/<str:temp>', inputData , name='inputData'),
    path('dashboard',selectAll, name='dashboard'),
    path('', index, name='index'),
]