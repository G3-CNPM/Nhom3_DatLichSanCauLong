
from django.urls import include, path
from . import views
app_name='qls'

urlpatterns = [
    path('',views.get_qls,name='qlsan'),
]