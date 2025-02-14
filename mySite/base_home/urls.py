from django.contrib import admin
from django.urls import path, include
from . import views
app_name='base'

urlpatterns = [
    path('', views.main, name='main'),
    path('register-page/', views.register, name='register'),
    path('login-page/', views.login, name='login'),
    path('don-hang', views.donhang, name='donhang'),
    path('san-pham', views.sanpham, name='sanpham'),
    path('tim-san', views.timsan, name='timsan'),
    path('trang-ca-nhan', views.trangcanhan, name='trangcanhan'),
    path('voucher', views.voucher, name='voucher'),
]