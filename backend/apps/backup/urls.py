from django.urls import path

from .views import (
    BackupCreateAPIView,
    BackupRestoreAPIView,
    BackupListAPIView,
    DatabaseInfoAPIView,
    BackupDeleteAPIView,   
)


urlpatterns = [

    # GET backup list
    path(
        "",
        BackupListAPIView.as_view()
    ),


    # Create backup
    path(
        "create/",
        BackupCreateAPIView.as_view()
    ),


    # Restore backup
    path(
        "restore/",
        BackupRestoreAPIView.as_view()
    ),


    # Database info report
    path(
        "info/",
        DatabaseInfoAPIView.as_view()
    ),
    path("delete/", BackupDeleteAPIView.as_view()),

]