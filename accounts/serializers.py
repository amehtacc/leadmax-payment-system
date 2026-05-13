from rest_framework import serializers

from .models import BankAccount


class BankAccountSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = BankAccount

        fields = '__all__'

        read_only_fields = [
            'id',
            'user',
            'balance',
            'created_at',
            'updated_at'
        ]

    def validate(self, attrs):

        user = self.context['request'].user

        total_accounts = BankAccount.objects.filter(
            user=user
        ).count()

        if total_accounts >= 3:

            raise serializers.ValidationError(
                "Maximum 3 bank accounts allowed"
            )

        return attrs


class TopUpSerializer(
    serializers.Serializer
):

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