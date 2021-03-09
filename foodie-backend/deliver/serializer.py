from rest_framework import serializers
from .models import Deliver


class DeliverSerializer(serializers.ModelSerializer):


    class Meta:
        model = Deliver
        fields = '__all__'

