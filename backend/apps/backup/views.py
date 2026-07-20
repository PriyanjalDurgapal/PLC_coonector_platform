from rest_framework.views import APIView
from rest_framework.response import Response

from .services import (
    create_backup,
    restore_backup,
    generate_db_info
)

import os
from datetime import datetime
from django.conf import settings



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

                "message": "Backup created",

                "output": output

            })


        except Exception as e:

            return Response({

                "success": False,

                "message": str(e)

            }, status=500)





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

                "message": "Database restored",

                "output": output

            })


        except Exception as e:
            print("RESTORE EXCEPTION:", repr(e))

            return Response({

                "success": False,

                "message": str(e) if str(e) else "Unknown error"

            }, status=500)





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


            return Response({

                "success": False,

                "message": str(e)

            }, status=500)





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

                "message": "Database info generated and sent",

                "file": output

            })


        except Exception as e:


            return Response({

                "success": False,

                "message": str(e)

            }, status=500)