from rest_framework import serializers

from user.serializer import UserSerializer
from .models import Deliver


class DeliverSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Deliver
        fields = ['user', 'nidNo']

    def validate_nidNo(self,value):
        if Deliver.objects.filter(nidNo= value).exists():
            raise serializers.ValidationError("Nid number is not unique")
        return value

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        deliver, created = Deliver.objects.update_or_create(user=user, nidNo=validated_data.pop('nidNo'))
        return deliver
