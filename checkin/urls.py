
from django.urls import include, path
from . import views
app_name='checkin'

urlpatterns = [
    path('', views.get_checkin,name='checkin'),
]
