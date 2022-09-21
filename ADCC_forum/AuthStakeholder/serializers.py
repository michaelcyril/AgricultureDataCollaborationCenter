from rest_framework import serializers
from .models import User, AdminProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'phone',
            'type',
            'created_at',
            'password',
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        if self.validated_data['type'] == 'farmer':
            first_name = self.validated_data['first_name']
            last_name = self.validated_data['last_name']
            email = self.validated_data['email']
            password = self.validated_data['password']
            username = self.validated_data['username']
            phone = self.validated_data['phone']
            type = self.validated_data['type']
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                            password=password, phone=phone, type=type)
            return user
        elif self.validated_data['type'] == 'admin':
            email = self.validated_data['email']
            password = self.validated_data['password']
            username = self.validated_data['username']
            phone = self.validated_data['phone']
            type = self.validated_data['type']
            user = User.objects.create_user(username=username, email=email,
                                            password=password, phone=phone, type=type)
            return user


class AdminProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminProfile
        fields = [
            'id',
            'user_id',
            'institute_logo',
            'institute',
            'wilaya_id',
            'type',
        ]
