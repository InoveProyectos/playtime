from django.urls import path, include
from stock.api.viewsets import *

urlpatterns = [
    path('api/', include('stock.api.routers')),
]