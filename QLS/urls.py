
from django.urls import include, path
from . import views
app_name='base'

urlpatterns = [
    path('',views.get_qls,name='qlsan'),
    path('thanhtoan/',views.get_thanhtoan,name='thanhtoan'),
    path('datsan/',views.get_datsan,name='datsan'),
    path('doanhthu/',views.get_doanhthu,name='doanhthu'),
]