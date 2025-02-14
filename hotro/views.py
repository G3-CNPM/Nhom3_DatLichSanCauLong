from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def get_hotro(request):
    return render(request,'hotro/hotro.html')