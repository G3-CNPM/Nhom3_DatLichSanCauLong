from django.urls import path
from . import views
app_name='login'

urlpatterns = [
    path("", views.get_login, name="login"),
    path("",views.get_register, name="register"),
]