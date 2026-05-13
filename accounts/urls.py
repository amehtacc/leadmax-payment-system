from django.urls import path

from .views import (

    CreateBankAccountView,

    UserBankAccountsView,

    DeleteBankAccountView,

    TopUpBankAccountView
)

urlpatterns = [

    # Add Bank Account
    path(
        '',
        CreateBankAccountView.as_view()
    ),

    # Get User Bank Accounts
    path(
        'list/',
        UserBankAccountsView.as_view()
    ),

    # Delete Bank Account
    path(
        '<int:pk>/delete/',
        DeleteBankAccountView.as_view()
    ),

    # Top-up Balance
    path(
        '<int:pk>/topup/',
        TopUpBankAccountView.as_view()
    ),
]