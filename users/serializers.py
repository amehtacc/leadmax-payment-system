from rest_framework import serializers

from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = [
            'id',
            'email',
            'full_name',
            'created_at'
        ]


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        min_length=6
    )

    class Meta:

        model = User

        fields = [
            'id',
            'email',
            'full_name',
            'password'
        ]

    def create(self, validated_data):

        return User.objects.create_user(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            password=validated_data['password']
        )
    

class UpdateUserSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = User

        fields = [
            'email',
            'full_name'
        ]

class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()

    password = serializers.CharField(
        write_only=True
    )

    def validate(self, attrs):

        email = attrs.get('email')

        password = attrs.get('password')

        user = authenticate(
            username=email,
            password=password
        )

        if not user:

            raise serializers.ValidationError(
                "Invalid email or password"
            )

        refresh = RefreshToken.for_user(user)

        return {

            'user': UserSerializer(user).data,

            'access': str(refresh.access_token),

            'refresh': str(refresh)
        }