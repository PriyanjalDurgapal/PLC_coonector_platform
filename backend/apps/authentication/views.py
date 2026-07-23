from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed

from apps.users.serializers import UserSerializer

from .serializers import LoginSerializer, LogoutSerializer
from .authentication_service import AuthenticationService, LogoutService
from .services.rate_limit_service import RateLimitService


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        # Get client IP
        ip = request.META.get("REMOTE_ADDR", "unknown")

        # Check if user is blocked
        if RateLimitService.is_blocked(username, ip):
            return Response(
                {
                    "success": False,
                    "message": "Too many failed login attempts. Please try again after 1 minute.",
                },
                status=status.HTTP_429_TOO_MANY_REQUESTS,
            )

        try:
            data = AuthenticationService.login(
                username=username,
                password=password,
            )

            # Successful login -> clear failed attempts
            RateLimitService.reset_attempts(username, ip)

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

        except AuthenticationFailed:
            # Wrong password -> increase failed attempts
            RateLimitService.record_failed_attempt(username, ip)
            raise


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