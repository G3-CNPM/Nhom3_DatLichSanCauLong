from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_login(request):
    return render(request,'Login/login.html')

def get_register(request):
    return render(request,'Register/register.html')