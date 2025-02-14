from django.shortcuts import render

# Create your views here.
def get_qls(request):
    return render(request,'QLS/qls.html')

def get_thanhtoan(request):
    return render(request,'QLS/thanhtoan.html')

def get_datsan(request):
    return render(request,'QLS/datsan.html')

def get_doanhthu(request):
    return render(request,'QLS/doanhthu.html')