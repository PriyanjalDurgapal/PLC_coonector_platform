from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken


class AuthenticationService:

    @staticmethod
    def login(username, password):
        user = authenticate(username=username, password=password)

        if user is None:
            raise AuthenticationFailed("Invalid username or password.")

        refresh = RefreshToken.for_user(user)

        return {
            "user": user,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }

class LogoutService:

    @staticmethod
    def logout(refresh_token: str):
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception:
            raise ValidationError("Invalid or expired refresh token.")