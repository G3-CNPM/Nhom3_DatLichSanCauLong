from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def register(request):
    return render(request, 'base_home/register.html')

def login(request):
    return render(request, 'base_home/login.html')

def main(request):
    return render(request, 'base_home/main.html')

def sanpham(request):
    return render(request, 'base_home/sanpham.html')

def timsan(request):
    return render(request, 'base_home/timsan.html')

def trangcanhan(request):
    return render(request, 'base_home/trangcanhan.html')

def voucher(request):
    return render(request, 'base_home/voucher.html')

def donhang(request):
    return render(request, 'base_home/donhang.html')