from django.shortcuts import render

# Create your views here.
def get_qls(request):
    return render(request,'QLS/qls.html')