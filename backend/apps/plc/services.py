from django.shortcuts import get_object_or_404
from .models import PLC, PLCTag, PLCOperationLog
from .tag_reader import PLCTagReader
class PLCService:

    @staticmethod
    def get_plcs():
        return PLC.objects.all()


    @staticmethod
    def get_plc_by_id(plc_id):
        return get_object_or_404(
            PLC,
            id=plc_id,
        )


    @staticmethod
    def create_plc(validated_data):
        return PLC.objects.create(
            **validated_data
        )


    @staticmethod
    def update_plc(plc, validated_data):

        for field, value in validated_data.items():
            setattr(
                plc,
                field,
                value,
            )

        plc.save()

        return plc


    @staticmethod
    def delete_plc(plc):

        plc.delete()


# =====================================================
# PLC TAG SERVICE
# =====================================================

class PLCTagService:

    @staticmethod
    def get_tags():

        return (
            PLCTag.objects
            .select_related("plc")
            .all()
        )


    @staticmethod
    def get_tag_by_id(tag_id):

        return (
            PLCTag.objects
            .select_related("plc")
            .get(id=tag_id)
        )


    @staticmethod
    def create_tag(validated_data):

        return PLCTag.objects.create(
            **validated_data
        )


    @staticmethod
    def update_tag(tag, validated_data):

        for key, value in validated_data.items():

            setattr(
                tag,
                key,
                value,
            )

        tag.save()

        return tag


    @staticmethod
    def delete_tag(tag):

        tag.delete()

class PLCOperationLogService:


    @staticmethod
    def get_logs():

        return (
            PLCOperationLog.objects
            .select_related(
                "user",
                "plc",
                "tag",
            )
            .all()
        )


# =====================================================
# PLC OPERATION LOG SERVICE
# =====================================================


class PLCOperationLogService:


    @staticmethod
    def get_logs():

        return (

            PLCOperationLog.objects

            .select_related(

                "user",

                "plc",

                "tag",

            )

            .all()

        )


# =====================================================
# PLC TAG READ SERVICE
# =====================================================

class PLCTagReadService:


    @staticmethod
    def read_tag(tag):

        return PLCTagReader.read_tag(
            tag
        )