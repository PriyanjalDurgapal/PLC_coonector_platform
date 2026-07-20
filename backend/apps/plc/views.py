from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .tag_reader import PLCTagReader
from .connection_service import plc_connection

from .tag_monitor import PLCTagMonitor
from .write_service import PLCWriteService


from .models import PLCTag


from .serializers import (
    PLCListSerializer,
    PLCCreateSerializer,
    PLCUpdateSerializer,

    PLCTagListSerializer,
    PLCTagCreateSerializer,
    PLCTagUpdateSerializer,
    PLCOperationLogSerializer,

   
    
)


from .services import (
    PLCService,
    PLCTagService,
    PLCOperationLogService,
    PLCTagReadService,
)


from .permissions import HasPermission


from .filters import PLCTagFilter



# =====================================================
# PLC LIST + CREATE
# =====================================================

class PLCListCreateView(APIView):

    permission_classes = [
        IsAuthenticated,
        HasPermission,
    ]


    permissions_map = {

        "GET": "plc.view_plc",

        "POST": "plc.add_plc",

    }


    def get(self, request):

        plcs = PLCService.get_plcs()


        serializer = PLCListSerializer(
            plcs,
            many=True,
        )


        return Response(
            {
                "success": True,
                "data": serializer.data,
            }
        )



    def post(self, request):

        serializer = PLCCreateSerializer(
            data=request.data,
        )


        serializer.is_valid(
            raise_exception=True,
        )


        plc = PLCService.create_plc(
            serializer.validated_data,
        )


        return Response(
            {
                "success": True,
                "message": "PLC created successfully.",
                "data": PLCListSerializer(plc).data,
            },
            status=status.HTTP_201_CREATED,
        )



# =====================================================
# PLC DETAIL
# =====================================================

class PLCDetailView(APIView):

    permission_classes = [
        IsAuthenticated,
        HasPermission,
    ]


    permissions_map = {

        "GET": "plc.view_plc",

        "PUT": "plc.change_plc",

        "DELETE": "plc.delete_plc",

    }



    def get(self, request, plc_id):

        plc = PLCService.get_plc_by_id(
            plc_id,
        )


        serializer = PLCListSerializer(
            plc,
        )


        return Response(
            {
                "success": True,
                "data": serializer.data,
            }
        )



    def put(self, request, plc_id):

        plc = PLCService.get_plc_by_id(
            plc_id,
        )


        serializer = PLCUpdateSerializer(
            plc,
            data=request.data,
            partial=True,
        )


        serializer.is_valid(
            raise_exception=True,
        )


        plc = PLCService.update_plc(
            plc,
            serializer.validated_data,
        )


        return Response(
            {
                "success": True,
                "message": "PLC updated successfully.",
                "data": PLCListSerializer(plc).data,
            }
        )



    def delete(self, request, plc_id):

        plc = PLCService.get_plc_by_id(
            plc_id,
        )


        PLCService.delete_plc(
            plc,
        )


        return Response(
            {
                "success": True,
                "message": "PLC deleted successfully.",
            }
        )



# =====================================================
# PLC CONNECT
# =====================================================

class PLCConnectView(APIView):

    permission_classes = [
        IsAuthenticated,
        HasPermission,
    ]


    permissions_map = {

        "POST": "plc.change_plc",

    }



    def post(self, request, plc_id):

        plc = PLCService.get_plc_by_id(
            plc_id,
        )


        result = plc_connection.connect(
            plc,
        )


        status_code = (

            status.HTTP_200_OK

            if result["success"]

            else status.HTTP_400_BAD_REQUEST

        )


        return Response(
            result,
            status=status_code,
        )



# =====================================================
# PLC DISCONNECT
# =====================================================

class PLCDisconnectView(APIView):

    permission_classes = [
        IsAuthenticated,
        HasPermission,
    ]


    permissions_map = {

        "POST": "plc.change_plc",

    }



    def post(self, request, plc_id):

        return Response(
            plc_connection.disconnect()
        )



# =====================================================
# PLC STATUS
# =====================================================

class PLCStatusView(APIView):

    permission_classes = [
        IsAuthenticated,
        HasPermission,
    ]


    permissions_map = {

        "GET": "plc.view_plc",

    }



    def get(self, request, plc_id):

        return Response(
            plc_connection.status()
        )



# =====================================================
# PLC TAG VIEWSET
# =====================================================

class PLCTagViewSet(viewsets.ModelViewSet):

    queryset = PLCTag.objects.all()


    serializer_class = PLCTagListSerializer



    permission_classes = [
        IsAuthenticated,
        HasPermission,
    ]



    permissions_map = {

        "GET": "plc.view_plctag",

        "POST": "plc.add_plctag",

        "PUT": "plc.change_plctag",

        "PATCH": "plc.change_plctag",

        "DELETE": "plc.delete_plctag",

    }



    filter_backends = [

        DjangoFilterBackend,

        SearchFilter,

        OrderingFilter,

    ]



    filterset_class = PLCTagFilter



    search_fields = [

        "name",

        "address",

    ]



    ordering_fields = [

        "name",

        "address",

        "created_at",

    ]



    ordering = [

        "name",

    ]



    def create(self, request, *args, **kwargs):

        serializer = PLCTagCreateSerializer(
            data=request.data
        )


        serializer.is_valid(
            raise_exception=True
        )


        tag = PLCTagService.create_tag(
            serializer.validated_data
        )


        return Response(
            {
                "success": True,
                "message": "PLC Tag created successfully.",
                "data": PLCTagListSerializer(tag).data,
            },
            status=status.HTTP_201_CREATED,
        )



    def update(self, request, *args, **kwargs):

        tag = self.get_object()


        serializer = PLCTagUpdateSerializer(
            tag,
            data=request.data,
            partial=True,
        )


        serializer.is_valid(
            raise_exception=True
        )


        tag = PLCTagService.update_tag(
            tag,
            serializer.validated_data,
        )


        return Response(
            {
                "success": True,
                "message": "PLC Tag updated successfully.",
                "data": PLCTagListSerializer(tag).data,
            }
        )



    def destroy(self, request, *args, **kwargs):

        tag = self.get_object()


        PLCTagService.delete_tag(
            tag
        )


        return Response(
            {
                "success": True,
                "message": "PLC Tag deleted successfully.",
            }
        )


# =====================================================
# PLC TAG VALUE READ
# =====================================================

class PLCTagValueView(APIView):


    permission_classes = [

        IsAuthenticated,

        HasPermission,

    ]


    permissions_map = {

        "GET": "plc.view_plctag",

    }



    def get(self, request, tag_id):


        tag = PLCTagService.get_tag_by_id(
            tag_id
        )


        result = PLCTagReader.read_tag(
            tag
        )


        return Response(
            result
        )



# =====================================================
# PLC LIVE TAG VALUES
# =====================================================

class PLCLiveTagsView(APIView):

    permission_classes = [
        IsAuthenticated,
        HasPermission,
    ]


    permissions_map = {
        "GET": "plc.view_plctag",
    }


    def get(self, request, plc_id):

        result = PLCTagMonitor.read_all_tags(
            plc_id
        )


        return Response(
            {
                "success": True,
                "data": result,
            }
        )

# =====================================================
# PLC TAG WRITE
# =====================================================

class PLCWriteView(APIView):

    permission_classes = [
        IsAuthenticated,
        HasPermission,
    ]


    permissions_map = {
        "POST": "plc.change_plctag",
    }


    def post(self, request, tag_id):

        tag = PLCTagService.get_tag_by_id(
            tag_id
        )


        value = request.data.get(
            "value"
        )


        if value is None:

            return Response(
                {
                    "success": False,
                    "message": "Value is required."
                },
                status=400
            )


        result = PLCWriteService.write_tag(
            tag,
            value,
            request.user
        )


        return Response(
            result
        )




# =====================================================
# PLC OPERATION LOG VIEW
# =====================================================


class PLCOperationLogListView(APIView):

    permission_classes = [

        IsAuthenticated,

        HasPermission,

    ]


    permissions_map = {

        "GET": "plc.view_plc",

    }



    def get(self, request):

        logs = PLCOperationLogService.get_logs()


        serializer = PLCOperationLogSerializer(

            logs,

            many=True,

        )


        return Response(

            {

                "success": True,

                "data": serializer.data,

            }

        )


# =====================================================
# PLC TAG READ VIEW
# =====================================================

class PLCTagReadView(APIView):

    permission_classes = [
        IsAuthenticated,
        HasPermission,
    ]


    permissions_map = {
        "GET": "plc.view_plc",
    }


    def get(self, request, tag_id):

        tag = PLCTagService.get_tag_by_id(
            tag_id
        )


        result = PLCTagReadService.read_tag(
            tag
        )


        return Response(
            result
        )