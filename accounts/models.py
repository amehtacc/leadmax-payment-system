from django.db import models

from django.conf import settings

from django.utils import timezone


class BankAccount(models.Model):

    user = models.ForeignKey(

        settings.AUTH_USER_MODEL,

        on_delete=models.CASCADE,

        related_name='bank_accounts'
    )

    bank_name = models.CharField(
        max_length=255
    )

    account_number = models.CharField(
        max_length=50,
        unique=True
    )

    balance = models.DecimalField(

        max_digits=12,

        decimal_places=2,

        default=0
    )

    created_at = models.DateTimeField(
        default=timezone.now
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return f"{self.user.email} - {self.account_number}"