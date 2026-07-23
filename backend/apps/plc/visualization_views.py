from rest_framework.viewsets import ModelViewSet

from .models import (
    PLCVisualizationObject,
)

from .serializers import (
    PLCVisualizationObjectSerializer,
)


class PLCVisualizationObjectViewSet(ModelViewSet):

    queryset = (
        PLCVisualizationObject.objects
        .select_related(
            "tag",
            "tag__plc",
            "tag__current_value",
        )
        .all()
    )

    serializer_class = (
        PLCVisualizationObjectSerializer
    )