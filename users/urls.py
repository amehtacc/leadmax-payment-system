from django.urls import path

from .views import (
    RegisterView,
    UserListView,
    UserProfileView,
    UpdateUserView,
    DeleteUserView,
    LoginView
)

from rest_framework_simplejwt.views import (
    TokenRefreshView
)

urlpatterns = [

    # User APIs
    path(
        'register/',
        RegisterView.as_view()
    ),

    path(
        '',
        UserListView.as_view()
    ),

    path(
        'profile/',
        UserProfileView.as_view()
    ),

    path(
        '<int:pk>/update/',
        UpdateUserView.as_view()
    ),

    path(
        '<int:pk>/delete/',
        DeleteUserView.as_view()
    ),

    # Auth APIs
    path(
        'login/',
        LoginView.as_view()
    ),

    path(
        'refresh/',
        TokenRefreshView.as_view()
    ),
]