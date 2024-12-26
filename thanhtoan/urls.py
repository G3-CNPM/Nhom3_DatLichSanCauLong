from django.urls import include, path
from . import views
app_name='thanhtoan'

urlpatterns = [
    path('',views.get_thanhtoan,name='thanhtoan'),
]