from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def register(request):
    return render(request, 'base_home/register.html')

def login(request):
    return render(request, 'base_home/login.html')

def main(request):
    return render(request, 'base_home/main.html')

#customer
def donhang(request):
    return render(request, 'customer/donhang.html')

def timsan(request):
    return render(request, 'customer/timsan.html')

def trangcanhan(request):
    return render(request, 'customer/trangcanhan.html')

def voucher(request):
    return render(request, 'customer/voucher.html')

def sanpham(request):
    return render(request, 'customer/sanpham.html')
