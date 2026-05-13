from drf_spectacular.utils import extend_schema

from django.db import transaction

from django.db.models import Q

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.permissions import (
    IsAuthenticated
)

from rest_framework import status

from .models import Transaction

from .serializers import (
    PaymentSerializer,
    TransactionSerializer
)

from accounts.models import BankAccount


# Do Payment
@extend_schema(
    request=PaymentSerializer
)
class DoPaymentView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = PaymentSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        data = serializer.validated_data

        sender_account_id = data[
            'sender_account_id'
        ]

        receiver_account_id = data[
            'receiver_account_id'
        ]

        amount = data['amount']

        # Prevent self transfer
        if (
            sender_account_id ==
            receiver_account_id
        ):

            transaction_obj = (
                Transaction.objects.create(

                    sender_account_id=
                    sender_account_id,

                    receiver_account_id=
                    receiver_account_id,

                    amount=amount,

                    status='FAILED',

                    failure_reason=(
                        "Cannot transfer "
                        "to same account"
                    )
                )
            )

            return Response(
                {
                    "message":
                    "Cannot transfer "
                    "to same account"
                },
                status=400
            )

        try:

            sender_account = (
                BankAccount.objects.get(

                    id=sender_account_id,

                    user=request.user
                )
            )

        except BankAccount.DoesNotExist:

            return Response(
                {
                    "message":
                    "Sender account invalid"
                },
                status=404
            )

        try:

            receiver_account = (
                BankAccount.objects.get(
                    id=receiver_account_id
                )
            )

        except BankAccount.DoesNotExist:

            Transaction.objects.create(

                sender_account=
                sender_account,

                receiver_account=
                sender_account,

                amount=amount,

                status='FAILED',

                failure_reason=(
                    "Receiver account "
                    "not found"
                )
            )

            return Response(
                {
                    "message":
                    "Receiver account "
                    "not found"
                },
                status=404
            )

        # Insufficient balance
        if sender_account.balance < amount:

            Transaction.objects.create(

                sender_account=
                sender_account,

                receiver_account=
                receiver_account,

                amount=amount,

                status='FAILED',

                failure_reason=(
                    "Insufficient balance"
                )
            )

            return Response(
                {
                    "message":
                    "Insufficient balance"
                },
                status=400
            )

        # Atomic Transaction
        with transaction.atomic():

            sender_account.balance -= amount

            receiver_account.balance += amount

            sender_account.save()

            receiver_account.save()

            transaction_obj = (
                Transaction.objects.create(

                    sender_account=
                    sender_account,

                    receiver_account=
                    receiver_account,

                    amount=amount,

                    status='SUCCESS'
                )
            )

        return Response({

            "message":
            "Payment successful",

            "transaction_id":
            transaction_obj.id
        })


# Get Transactions List
@extend_schema(
    responses=TransactionSerializer(many=True)
)
class UserTransactionsView(
    APIView
):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        transactions = (

            Transaction.objects.filter(

                Q(
                    sender_account__user=
                    request.user
                ) |

                Q(
                    receiver_account__user=
                    request.user
                )
            )

            .distinct()

            .order_by('-created_at')
        )

        serializer = (
            TransactionSerializer(
                transactions,
                many=True
            )
        )

        return Response(
            serializer.data
        )