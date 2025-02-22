from django.contrib import admin
from django.urls import path, include
from . import views
app_name='base'

urlpatterns = [
    path('', views.main, name='main'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('don_hang', views.donhang, name='donhang'),
    path('san_pham', views.sanpham, name='sanpham'),
    path('tim_san', views.timsan, name='timsan'),
    path('trang_ca_nhan', views.trangcanhan, name='trangcanhan'),
    path('voucher', views.voucher, name='voucher'),
]