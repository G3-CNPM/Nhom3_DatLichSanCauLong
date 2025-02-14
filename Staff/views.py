from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def get_checkin(request):
    return render(request,'Staff/checkin.html')
def get_kttrangthai(request):
    return render(request,'Staff/kttrangthai.html')
def get_hotro(request):
    return render(request,'Staff/hotro.html')
def get_hoadon(request):
    return render(request,'Staff/hoadon.html')