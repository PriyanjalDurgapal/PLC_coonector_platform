from rest_framework.views import APIView
from rest_framework.response import Response

from .services import (
    create_backup,
    restore_backup,
    generate_db_info,
    delete_backup
)

import os
from datetime import datetime
from django.conf import settings


def format_error(error):

    error = str(error).strip()

    # Remove empty lines
    lines = [
        line.strip()
        for line in error.splitlines()
        if line.strip()
    ]

    # Remove duplicate lines
    unique_lines = []

    for line in lines:

        if line not in unique_lines:
            unique_lines.append(line)

    return "\n".join(unique_lines)


class BackupCreateAPIView(APIView):

    def post(self, request):

        try:

            output = create_backup(
                request.data["db_name"],
                request.data["db_user"],
                request.data["db_host"],
                request.data["db_password"]
            )

            return Response({

                "success": True,

                "message": "Backup created successfully.",

                "output": output

            })

        except Exception as e:

            print("BACKUP CREATE ERROR:", repr(e))

            return Response({

                "success": False,

                "message": format_error(e)

            }, status=400)


class BackupRestoreAPIView(APIView):

    def post(self, request):

        try:

            output = restore_backup(

                request.data["backup_file"],
                request.data["db_name"],
                request.data["db_user"],
                request.data["db_host"],
                request.data["db_password"]

            )

            return Response({

                "success": True,

                "message": "Database restored successfully.",

                "output": output

            })

        except Exception as e:

            print("RESTORE ERROR:", repr(e))

            return Response({

                "success": False,

                "message": format_error(e)

            }, status=400)


class BackupListAPIView(APIView):

    def get(self, request):

        try:

            backup_dir = os.path.join(
                settings.BASE_DIR,
                "db_backup"
            )

            if not os.path.exists(backup_dir):

                return Response({

                    "success": True,

                    "data": []

                })

            files = []

            for filename in os.listdir(backup_dir):

                if filename.endswith(".sql.gz"):

                    file_path = os.path.join(
                        backup_dir,
                        filename
                    )

                    created_time = os.path.getctime(
                        file_path
                    )

                    files.append({

                        "id": filename,

                        "filename": filename,

                        "createdOn": datetime.fromtimestamp(
                            created_time
                        ).strftime(
                            "%Y-%m-%d %H:%M:%S"
                        )

                    })

            return Response({

                "success": True,

                "data": files

            })

        except Exception as e:

            print("BACKUP LIST ERROR:", repr(e))

            return Response({

                "success": False,

                "message": format_error(e)

            }, status=400)


class DatabaseInfoAPIView(APIView):

    def post(self, request):

        try:

            output = generate_db_info(

                request.data["db_name"],
                request.data["db_user"],
                request.data["db_host"],
                request.data["db_password"],
                request.data["email"]

            )

            return Response({

                "success": True,

                "message": "Database information generated successfully.",

                "file": output

            })

        except Exception as e:

            print("DATABASE INFO ERROR:", repr(e))

            return Response({

                "success": False,

                "message": format_error(e)

            }, status=400)


class BackupDeleteAPIView(APIView):

    def post(self, request):

        try:

            output = delete_backup(
                request.data["backup_file"]
            )

            return Response({

                "success": True,

                "message": output

            })

        except Exception as e:

            print("DELETE BACKUP ERROR:", repr(e))

            return Response({

                "success": False,

                "message": format_error(e)

            }, status=400)