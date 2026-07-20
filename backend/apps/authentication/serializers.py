from rest_framework import serializers





class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},
    )


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()





