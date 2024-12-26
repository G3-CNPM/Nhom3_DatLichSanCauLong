
from django.urls import include, path
from . import views
app_name='datsan'

urlpatterns = [
    path('',views.get_datsan,name='datsan'),
]