from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Users
from .forms import UserForm

# Create your views here.

def register(request):
    submitted = False
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserForm()
            return HttpResponseRedirect('/register?submitted=True')
            
        
    else:
        form = UserForm()
        if 'submitted' in request.GET:
            submitted = True
        
    return render(request, 'base_home/register.html', {'form':form, 'submitted':submitted})

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
    all_user = Users.objects.all
    return render(request, 'customer/trangcanhan.html', {'all':all_user})

def voucher(request):
    return render(request, 'customer/voucher.html')

def sanpham(request):
    return render(request, 'customer/sanpham.html')
