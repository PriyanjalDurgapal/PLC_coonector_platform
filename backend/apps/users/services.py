from django.contrib.auth.hashers import make_password

from .models import User
from apps.rbac.models import Role
from django.contrib.auth.hashers import make_password


class UserService:
    """
    Business logic related to users.
    """


    @staticmethod
    def get_users():

        return (
            User.objects
            .prefetch_related(
                "roles",
                "roles__permissions"
            )
            .all()
        )


    @staticmethod
    def get_user_by_id(user_id):

        return (
            User.objects
            .prefetch_related(
                "roles",
                "roles__permissions"
            )
            .get(
                id=user_id
            )
        )


    @staticmethod
    def create_user(data):

        roles = data.pop(
            "roles",
            []
        )

        password = data.pop(
            "password"
        )


        user = User.objects.create(
            **data,
            password=make_password(password)
        )


        if roles:

            role_objects = Role.objects.filter(
                id__in=roles
            )

            user.roles.set(
                role_objects
            )


        return user


    @staticmethod
    def update_user(user, data):

        roles = data.pop(
            "roles",
            None
        )


        for field, value in data.items():

            setattr(
                user,
                field,
                value
            )


        user.save()


        if roles is not None:

            role_objects = Role.objects.filter(
                id__in=roles
            )

            user.roles.set(
                role_objects
            )


        return user


    @staticmethod
    def delete_user(user):

        user.delete()

    
    @staticmethod
    def reset_password(user, password):

        user.password = make_password(password)

        user.save()

        return user