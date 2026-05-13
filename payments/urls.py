from django.urls import path

from .views import (

    DoPaymentView,

    UserTransactionsView
)

urlpatterns = [

    # Do Payment
    path(
        '',
        DoPaymentView.as_view()
    ),

    # Transactions List
    path(
        'transactions/',
        UserTransactionsView.as_view()
    ),
]