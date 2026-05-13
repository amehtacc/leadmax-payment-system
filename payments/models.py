from django.db import models

from django.utils import timezone

from accounts.models import BankAccount


class Transaction(models.Model):

    STATUS_CHOICES = [

        ('SUCCESS', 'SUCCESS'),

        ('FAILED', 'FAILED'),
    ]

    sender_account = models.ForeignKey(

        BankAccount,

        on_delete=models.CASCADE,

        related_name='sent_transactions'
    )

    receiver_account = models.ForeignKey(

        BankAccount,

        on_delete=models.CASCADE,

        related_name='received_transactions'
    )

    amount = models.DecimalField(

        max_digits=12,

        decimal_places=2
    )

    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES
    )

    failure_reason = models.TextField(

        blank=True,

        null=True
    )

    created_at = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):

        return (
            f"{self.sender_account} -> "
            f"{self.receiver_account}"
        )