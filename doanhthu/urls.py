
from django.urls import include, path
from . import views
app_name='dt'

urlpatterns = [
    path('',views.get_doanhthu,name='dt'),
]