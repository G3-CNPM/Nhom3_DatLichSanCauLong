from django.urls import include, path
from . import views
app_name= 'Admin'
urlpatterns = [
    path('',views.get_QLTK, name='QuanLyTaiKhoan'),
]