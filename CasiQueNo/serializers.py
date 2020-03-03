from rest_framework import serializers
from .models import CasiQueNo

class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasiQueNo
        fields = ('id', 'type', 'value')