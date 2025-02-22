from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Users
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm

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


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have registered successfully! Welcome!"))
            return redirect('home')
        else:
            messages.success(request, ("There wax a problem registering, please try again..."))
            return redirect('register')
    else:

    return render(request, 'register.html', {'form':form})
