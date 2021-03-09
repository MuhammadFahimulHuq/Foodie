from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=5)
    password = serializers.CharField(min_length=5, write_only=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(min_length=3)
    last_name = serializers.CharField(min_length=3)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'phoneNo', 'first_name', 'last_name', 'address', 'dateOfBirth']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        norm_email = value.lower()
        if User.objects.filter(email=norm_email).exists():
            raise serializers.ValidationError("Not unique email")
        return norm_email

    def validate_username(self, value):
        norm_username = value.lower()
        if User.objects.filter(username=norm_username).exists():
            raise serializers.ValidationError("Not unique username")
        return norm_username

    def validate_phoneNo(self, value):
        norm_phoneNo = value.lower()
        if User.objects.filter(phoneNo=norm_phoneNo).exists():
            raise serializers.ValidationError("Not unique phone number")
        return norm_phoneNo

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
