from django.shortcuts import render

# Create your views here.
def get_QLTK(request):
    return render(request, 'Admin/QuanLyTaiKhoan.html')
def get_QLSCL(request):
    return render(request, 'Admin/QuanLySanCauLong.html')
def get_LSTD(request):
    return render(request, 'Admin/LichSuThayDoi.html')
def get_BC(request):
    return render(request, 'Admin/BaoCao.html')

