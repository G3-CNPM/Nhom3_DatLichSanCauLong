from django.contrib import admin
from .models import Users, Vatdung, Doannuoc, Booking, Payment
# Register your models here.

admin.site.register(Users)
admin.site.register(Vatdung)
admin.site.register(Doannuoc)
admin.site.register(Booking)
admin.site.register(Payment)