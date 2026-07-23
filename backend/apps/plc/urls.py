from django.urls import path, include

from rest_framework.routers import DefaultRouter


from .views import (
    PLCListCreateView,
    PLCDetailView,
    PLCConnectView,
    PLCDisconnectView,
    PLCStatusView,
    PLCTagViewSet,
    PLCTagValueView,
    PLCLiveTagsView,
    PLCWriteView,
    PLCOperationLogListView,
    PLCTagReadView,
    PLCVisualizationLiveView,
)

from .visualization_views import (
    PLCVisualizationObjectViewSet,
)


router = DefaultRouter()

router.register(
    "tags",
    PLCTagViewSet,
    basename="plc-tags",
)

router.register(
    "visualizations",
    PLCVisualizationObjectViewSet,
    basename="plc-visualizations",
)


urlpatterns = [

    # ==========================
    # PLC APIs
    # ==========================

    path(
        "",
        PLCListCreateView.as_view(),
        name="plc-list",
    ),

    path(
        "<int:plc_id>/",
        PLCDetailView.as_view(),
        name="plc-detail",
    ),

    path(
        "<int:plc_id>/connect/",
        PLCConnectView.as_view(),
        name="plc-connect",
    ),

    path(
        "<int:plc_id>/disconnect/",
        PLCDisconnectView.as_view(),
        name="plc-disconnect",
    ),

    path(
        "<int:plc_id>/status/",
        PLCStatusView.as_view(),
        name="plc-status",
    ),

    # ==========================
    # PLC TAG APIs
    # ==========================

    path(
        "",
        include(router.urls),
    ),

    path(
        "tags/<int:tag_id>/value/",
        PLCTagValueView.as_view(),
        name="plc-tag-value",
    ),

    path(
        "<int:plc_id>/tags/live/",
        PLCLiveTagsView.as_view(),
        name="plc-live-tags",
    ),

    path(
        "tags/<int:tag_id>/write/",
        PLCWriteView.as_view(),
        name="plc-tag-write",
    ),

    path(
        "logs/",
        PLCOperationLogListView.as_view(),
        name="plc-operation-logs",
    ),

    path(
        "tags/<int:tag_id>/read/",
        PLCTagReadView.as_view(),
        name="tag-read",
    ),
        path(
        "visualizations/live/",
        PLCVisualizationLiveView.as_view(),
        name="visualization-live",
    ),
]