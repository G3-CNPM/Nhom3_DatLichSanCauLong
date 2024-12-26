from django.urls import include, path
from . import views
app_name='kttrangthai'

urlpatterns = [
    path('', views.get_kttrangthai,name='kttrangthai'),
]