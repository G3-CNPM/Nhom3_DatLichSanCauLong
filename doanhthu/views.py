from django.shortcuts import render

# Create your views here.
def get_doanhthu(request):
    return render(request,'doanhthu/doanhthu.html')