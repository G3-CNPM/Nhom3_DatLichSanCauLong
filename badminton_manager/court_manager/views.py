from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Booking, Revenue
from .serializers import BookingSerializer, RevenueSerializer
from django.db.models import Sum
from datetime import datetime, timedelta

# Home view to render the index.html page
def home_view(request):
    return render(request, 'index.html')

# API view to register booking
@api_view(['POST'])
def register_booking(request):
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Booking registered successfully"}, status=201)
    return Response(serializer.errors, status=400)

# API view to get revenue
@api_view(['GET'])
def get_revenue(request):
    filter_type = request.GET.get('filter', 'daily')
    today = datetime.now().date()

    if filter_type == 'daily':
        revenues = Revenue.objects.filter(date=today)
    elif filter_type == 'weekly':
        start_week = today - timedelta(days=today.weekday())
        revenues = Revenue.objects.filter(date__gte=start_week)
    elif filter_type == 'monthly':
        revenues = Revenue.objects.filter(date__month=today.month)
    else:
        return Response({"error": "Invalid filter type"}, status=400)

    total_revenue = revenues.aggregate(total=Sum('total_revenue'))['total'] or 0
    serializer = RevenueSerializer(revenues, many=True)
    return Response({"total_revenue": total_revenue, "details": serializer.data})
