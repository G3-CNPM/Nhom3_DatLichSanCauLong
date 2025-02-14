
from django.urls import include, path
from . import views
app_name='base'

urlpatterns = [
    path('', views.get_checkin,name='checkin'),
    path('kttrangthai/', views.get_kttrangthai,name='kttrangthai'),
    path('hotro/', views.get_hotro,name='hotro'),
    path('hoadon/', views.get_hoadon,name='hoadon'),
]
