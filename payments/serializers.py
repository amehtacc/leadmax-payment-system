from rest_framework import serializers

from .models import Transaction


class TransactionSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Transaction

        fields = '__all__'


class PaymentSerializer(
    serializers.Serializer
):

    sender_account_id = (
        serializers.IntegerField()
    )

    receiver_account_id = (
        serializers.IntegerField()
    )

    amount = serializers.DecimalField(

        max_digits=12,

        decimal_places=2
    )

    def validate_amount(
        self,
        value
    ):

        if value <= 0:

            raise serializers.ValidationError(
                "Amount must be greater than 0"
            )

        return value