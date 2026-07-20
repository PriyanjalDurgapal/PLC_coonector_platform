from django.urls import path

from .views import (
    UserListCreateView,
    UserDetailView,
    UserResetPasswordView,
)


urlpatterns = [

    path(
        "",
        UserListCreateView.as_view(),
        name="users"
    ),

    path(
        "<int:user_id>/",
        UserDetailView.as_view(),
        name="user-detail"
    ),
    path(
    "<int:user_id>/reset-password/",
    UserResetPasswordView.as_view(),
    name="reset-password"
    ),

]