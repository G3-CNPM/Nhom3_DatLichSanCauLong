
from django.urls import include, path
from . import views
app_name='hotro'

urlpatterns = [
    path('', views.get_hotro,name='hotro'),
]