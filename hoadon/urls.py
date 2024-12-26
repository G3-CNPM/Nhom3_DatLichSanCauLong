from django.urls import include, path
from . import views
app_name = 'hoadon'

urlpatterns = [
    path('', views.get_hoadon,name='hoadon'),
]
