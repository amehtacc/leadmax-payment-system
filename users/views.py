from drf_spectacular.utils import extend_schema

from rest_framework import generics

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.permissions import (
    IsAuthenticated
)

from .models import User

from .serializers import (
    UserSerializer,
    RegisterSerializer,
    UpdateUserSerializer,
    LoginSerializer
)


# Create User
@extend_schema(
    request=RegisterSerializer,
    responses=UserSerializer
)
class RegisterView(
    generics.CreateAPIView
):

    queryset = User.objects.all()

    serializer_class = RegisterSerializer


# Get Users List
@extend_schema(
    responses=UserSerializer(many=True)
)
class UserListView(
    generics.ListAPIView
):

    queryset = User.objects.all()

    serializer_class = UserSerializer

    permission_classes = [IsAuthenticated]


# Get User Profile
@extend_schema(
    responses=UserSerializer
)
class UserProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        serializer = UserSerializer(
            request.user
        )

        return Response(serializer.data)


# Update User
@extend_schema(
    request=UpdateUserSerializer,
    responses=UserSerializer
)
class UpdateUserView(
    generics.UpdateAPIView
):

    serializer_class = (
        UpdateUserSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):

        return User.objects.filter(
            id=self.request.user.id
        )
    

# Delete User
@extend_schema(
    responses={204: None}
)
class DeleteUserView(
    generics.DestroyAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):

        return User.objects.filter(
            id=self.request.user.id
        )


# Login User
@extend_schema(
    request=LoginSerializer
)
class LoginView(APIView):

    def post(self, request):

        serializer = LoginSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        return Response(
            serializer.validated_data
        )