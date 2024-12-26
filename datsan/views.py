from django.shortcuts import render

# Create your views here.
def get_datsan(request):
    return render(request,'datsan/datsan.html')