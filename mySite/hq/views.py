from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#admin
def baocao(request):
    return render(request, 'hq/admin_user/baocao.html')

def lichsu(request):
    return render(request, 'hq/admin_user/lichsu.html')

def sancaulong(request):
    return render(request, 'hq/admin_user/sancaulong.html')

def taikhoan(request):
    return render(request, 'hq/admin_user/taikhoan.html')

#manager
def datsan(request):
    return render(request, 'hq/manager/datsan.html')

def doanhthu(request):
    return render(request, 'hq/manager/doanhthu.html')

def qls(request):
    return render(request, 'hq/manager/qls.html')

def thanhtoan(request):
    return render(request, 'hq/manager/thanhtoan.html')

#staff
def checkin(request):
    return render(request, 'hq/staff/checkin.html')

def hoadon(request):
    return render(request, 'hq/staff/hoadon.html')

def hotro(request):
    return render(request, 'hq/staff/hotro.html')

def kttrangthai(request):
    return render(request, 'hq/staff/kttrangthai.html')
