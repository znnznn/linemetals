from django.contrib.auth import get_user_model
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50, min_length=2, required=True)
    last_name = serializers.CharField(max_length=50, min_length=2, required=True)
    role = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'role', )
        read_only_fields = ['role', 'email']


class LoginSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[self.username_field] = serializers.EmailField()

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data['user'] = UserSerializer(self.user).data

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data
