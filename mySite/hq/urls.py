from django.urls import path, include
from . import views
app_name='admin_user'

urlpatterns = [
    #admin
    path('tai-khoan/', views.taikhoan, name='taikhoan'),
    path('san-cau-long/', views.sancaulong, name='sancaulong'),
    path('lich-su/', views.lichsu, name='lichsu'),
    path('bao-cao/', views.baocao, name='baocao'),
    #manager
    path('dat-san/', views.datsan, name='datsan'),
    path('doanh-thu/', views.doanhthu, name='doanhthu'),
    path('quan-li-san/', views.qls, name='qls'),
    path('thanh-toan/', views.thanhtoan, name='thanhtoan'),
    #staff
    path('check-in/', views.checkin, name='checkin'),
    path('hoa-don/', views.hoadon, name='hoadon'),
    path('kiem-tra-trang-thai/', views.kttrangthai, name='kttrangthai'),
    path('ho-tro/', views.hotro, name='hotro'),
]