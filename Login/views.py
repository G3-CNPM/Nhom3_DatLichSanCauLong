from django.shortcuts import render

# Create your views here.
def get_login(request):
    return render(request, 'Login/login.html')