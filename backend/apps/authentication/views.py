from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoginSerializer
from .services import AuthenticationService

from rest_framework.permissions import IsAuthenticated
from apps.users.serializers import UserSerializer


from .serializers import LogoutSerializer
from .services import LogoutService


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = AuthenticationService.login(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )

        return Response(
            {
                "success": True,
                "message": "Login successful.",
                "data": {
                    "user": {
                        "id": data["user"].id,
                        "username": data["user"].username,
                        "email": data["user"].email,
                        "first_name": data["user"].first_name,
                        "last_name": data["user"].last_name,
                    },
                    "access": data["access"],
                    "refresh": data["refresh"],
                },
            },
            status=status.HTTP_200_OK,
        )


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)

        return Response(
            {
                "success": True,
                "message": "User fetched successfully.",
                "data": serializer.data,
            }
        )


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        LogoutService.logout(
            serializer.validated_data["refresh"]
        )

        return Response(
            {
                "success": True,
                "message": "Logout successful.",
            },
            status=status.HTTP_200_OK,
        )