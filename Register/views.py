from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def get_reg(request):
    return render(request,'Register/register.html')