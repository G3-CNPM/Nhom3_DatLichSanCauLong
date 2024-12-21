from django.urls import path
from . import views
app_name='reg'

urlpatterns = [
    path("", views.get_reg, name="register"),
]