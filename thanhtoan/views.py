from django.shortcuts import render

# Create your views here.
def get_thanhtoan(request):
    return render(request,'thanhtoan/thanhtoan.html')