from django.shortcuts import render

# Create your views here.
def get_SanPham(request):
    return render(request, 'SanPham/SanPham.html')