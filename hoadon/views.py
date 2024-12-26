from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def get_hoadon(request):
    return render(request,'hoadon/hoadon.html')