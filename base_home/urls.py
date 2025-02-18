from django.contrib import admin
from django.urls import path, include
from . import views
app_name='base'

urlpatterns = [
    path('', views.main, name='main'),
    path('register-page/', views.register, name='register'),
    path('login-page/', views.login, name='login'),
    path('sanpham/', views.sanpham, name='sanpham'),
    path('timsan/', views.timsan, name='timsan'),
    path('trangcanhan/', views.trangcanhan, name='trangcanhan'),
    path('voucher/', views.voucher, name='voucher'),
    path('donhang/', views.donhang, name='donhang'),
]
