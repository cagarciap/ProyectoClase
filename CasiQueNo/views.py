from django.shortcuts import render
from rest_framework import viewsets
from .models import CasiQueNo
from .serializers import MeasureSerializer

class MeasureViewSet(viewsets.ModelViewSet):
    queryset = CasiQueNo.objects.all().order_by('-created')
    serializer_class = MeasureSerializer

# Create your views here.
