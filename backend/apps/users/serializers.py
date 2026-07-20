from rest_framework import serializers

from .models import User




class UserListSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying users.
    Used in user listing APIs.
    """

    roles = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "employee_id",
            "is_active",
            "is_staff",
            "roles",
        )

    def get_roles(self, obj):
        return list(
            obj.roles.values_list(
                "name",
                flat=True
            )
        )


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating users.
    """

    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    roles = serializers.ListField(
        child=serializers.IntegerField(),
        required=False
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "employee_id",
            "roles",
        )

    def validate_username(self, value):

        if User.objects.filter(
            username=value
        ).exists():
            raise serializers.ValidationError(
                "Username already exists."
            )

        return value


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating users.
    """

    roles = serializers.ListField(
        child=serializers.IntegerField(),
        required=False
    )


    class Meta:

        model = User

        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "employee_id",
            "is_active",
            "roles",
        )



    def update(self, instance, validated_data):

        roles = validated_data.pop(
            "roles",
            None
        )


        # Update normal fields

        for attr, value in validated_data.items():

            setattr(
                instance,
                attr,
                value
            )


        instance.save()



        # Update roles

        if roles is not None:

            instance.roles.set(
                roles
            )


        return instance


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer used by authentication APIs.
    Returns current logged-in user information.
    """

    roles = serializers.SerializerMethodField()
    permissions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "roles",
            "permissions",
        )

    def get_roles(self, obj):

        return list(
            obj.roles.values(
                "id",
                "name"
            )
        )

    def get_permissions(self, obj):

        permissions = set()

        for role in obj.roles.all():
            for permission in role.permissions.all():
                permissions.add(permission.codename)

        return list(permissions)

    
class ResetPasswordSerializer(serializers.Serializer):

    password = serializers.CharField(
        min_length=8,
        write_only=True
    )