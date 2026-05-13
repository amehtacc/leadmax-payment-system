from drf_spectacular.utils import extend_schema

from rest_framework import generics

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.permissions import (
    IsAuthenticated
)

from rest_framework import status

from .models import BankAccount

from .serializers import (
    BankAccountSerializer,
    TopUpSerializer
)


# Add User Bank Account
@extend_schema(
    request=BankAccountSerializer,
    responses=BankAccountSerializer
)
class CreateBankAccountView(
    generics.CreateAPIView
):

    serializer_class = BankAccountSerializer    

    permission_classes = [IsAuthenticated]

    def perform_create(
        self,
        serializer
    ):

        serializer.save(
            user=self.request.user
        )


# Get User Bank Accounts
@extend_schema(
    responses=BankAccountSerializer(many=True)
)
class UserBankAccountsView(
    generics.ListAPIView
):

    serializer_class = (
        BankAccountSerializer
    )

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return BankAccount.objects.filter(
            user=self.request.user
        )


# Delete Bank Account
@extend_schema(
    responses={204: None}
)
class DeleteBankAccountView(
    generics.DestroyAPIView
):

    serializer_class = (
        BankAccountSerializer
    )

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return BankAccount.objects.filter(
            user=self.request.user
        )


# Top-up Bank Account
@extend_schema(
    request=TopUpSerializer
)
class TopUpBankAccountView(
    APIView
):

    permission_classes = [IsAuthenticated]

    def post(
        self,
        request,
        pk
    ):

        serializer = TopUpSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        try:

            bank_account = (
                BankAccount.objects.get(
                    id=pk,
                    user=request.user
                )
            )

        except BankAccount.DoesNotExist:

            return Response(
                {
                    "message":
                    "Bank account not found"
                },
                status=404
            )

        amount = serializer.validated_data[
            'amount'
        ]

        bank_account.balance += amount

        bank_account.save()

        return Response({

            "message":
            "Balance topped up successfully",

            "new_balance":
            bank_account.balance
        })