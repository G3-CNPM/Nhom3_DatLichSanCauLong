from django.urls import path
from .views import register_booking, get_revenue

urlpatterns = [
    path('api/register/', register_booking, name='register_booking'),
    path('api/revenue/', get_revenue, name='get_revenue'),
]
