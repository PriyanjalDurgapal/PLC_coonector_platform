from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


from .serializers import (
    UserListSerializer,
    UserCreateSerializer,
    UserUpdateSerializer,
    ResetPasswordSerializer,
)

from .services import UserService
from .permissions import HasPermission



class UserListCreateView(APIView):

    permission_classes = [
        IsAuthenticated,
        HasPermission,
    ]


    permissions_map = {
        "GET": "view_user",
        "POST": "add_user",
    }


    def get(self, request):

        self.required_permission = "view_user"


        users = UserService.get_users()


        # Search filter
        search = request.GET.get("search")

        if search:
            users = users.filter(
                username__icontains=search
            ) | users.filter(
                email__icontains=search
            ) | users.filter(
                employee_id__icontains=search
            )


        # Active filter
        is_active = request.GET.get("is_active")

        if is_active:

            users = users.filter(
                is_active=is_active.lower() == "true"
            )


        # Role filter
        role = request.GET.get("role")

        if role:

            users = users.filter(
                roles__name__iexact=role
            )


        # Pagination
        paginator = PageNumberPagination()

        paginator.page_size = 20


        paginated_users = paginator.paginate_queryset(
            users,
            request
        )


        serializer = UserListSerializer(
            paginated_users,
            many=True
        )


        return paginator.get_paginated_response(
            {
                "success": True,
                "data": serializer.data
            }
        )



    def post(self, request):

        self.required_permission = "add_user"


        serializer = UserCreateSerializer(
            data=request.data
        )


        serializer.is_valid(
            raise_exception=True
        )


        user = UserService.create_user(
            serializer.validated_data
        )


        return Response(
            {
                "success": True,
                "message": "User created successfully.",
                "data": UserListSerializer(user).data,
            },
            status=status.HTTP_201_CREATED
        )





class UserDetailView(APIView):

    permission_classes = [
        IsAuthenticated,
        HasPermission,
    ]


    permissions_map = {
        "GET": "view_user",
        "PUT": "change_user",
        "DELETE": "delete_user",
    }



    def get(self, request, user_id):

        self.required_permission = "view_user"


        user = UserService.get_user_by_id(
            user_id
        )


        serializer = UserListSerializer(
            user
        )


        return Response(
            {
                "success": True,
                "data": serializer.data,
            }
        )




    def put(self, request, user_id):

        self.required_permission = "change_user"


        user = UserService.get_user_by_id(
            user_id
        )


        serializer = UserUpdateSerializer(
            user,
            data=request.data,
            partial=True
        )


        serializer.is_valid(
            raise_exception=True
        )


        user = UserService.update_user(
            user,
            serializer.validated_data
        )


        return Response(
            {
                "success": True,
                "message": "User updated successfully.",
                "data": UserListSerializer(user).data,
            }
        )




    def delete(self, request, user_id):

        self.required_permission = "delete_user"


        user = UserService.get_user_by_id(
            user_id
        )


        UserService.delete_user(
            user
        )


        return Response(
            {
                "success": True,
                "message": "User deleted successfully."
            }
        )

class UserResetPasswordView(APIView):

    permission_classes = [
        IsAuthenticated,
        HasPermission,
    ]


    permissions_map = {
        "POST": "change_user",
    }



    def post(self, request, user_id):

        self.required_permission = "change_user"


        user = UserService.get_user_by_id(
            user_id
        )


        serializer = ResetPasswordSerializer(
            data=request.data
        )


        serializer.is_valid(
            raise_exception=True
        )


        UserService.reset_password(
            user,
            serializer.validated_data["password"]
        )


        return Response(
            {
                "success": True,
                "message": "Password reset successfully."
            }
        )