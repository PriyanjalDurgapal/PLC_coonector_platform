from .connection_service import plc_connection
from .models import PLCOperationLog



class PLCWriteService:


    @staticmethod
    def write_tag(tag, value, user=None):


        # Check PLC connection

        if not plc_connection.is_connected(
            tag.plc.id
        ):

            return {

                "success": False,

                "message": "PLC is not connected."

            }



        # Check writable permission

        if not tag.is_writable:

            return {

                "success": False,

                "message": "This tag is read-only."

            }



        try:

            client = plc_connection.client


            old_value = None



            # =========================
            # READ OLD VALUE
            # =========================

            try:

                if tag.data_type in [

                    "INT",
                    "WORD",

                ]:


                    old_value = client.batchread_wordunits(

                        tag.address,

                        1,

                    )[0]



                elif tag.data_type == "BOOL":


                    old_value = client.batchread_bitunits(

                        tag.address,

                        1,

                    )[0]



                print(
                    "OLD VALUE FOUND:",
                    old_value
                )



            except Exception as e:


                print(
                    "OLD VALUE READ ERROR:",
                    e
                )


                old_value = None



            # =========================
            # BOOL
            # =========================

            if tag.data_type == "BOOL":


                client.batchwrite_bitunits(

                    tag.address,

                    [bool(value)]

                )



            # =========================
            # INT / WORD
            # =========================

            elif tag.data_type in [

                "INT",
                "WORD",

            ]:


                client.batchwrite_wordunits(

                    tag.address,

                    [int(value)]

                )



            # =========================
            # REAL / FLOAT
            # =========================

            elif tag.data_type in [

                "REAL",
                "FLOAT",

            ]:


                words = PLCWriteService.float_to_words(

                    float(value)

                )


                client.batchwrite_wordunits(

                    tag.address,

                    words

                )



            else:


                return {

                    "success": False,

                    "message":
                    "Unsupported data type."

                }



            # =========================
            # CREATE AUDIT LOG
            # =========================

            PLCOperationLog.objects.create(

                user=user,

                plc=tag.plc,

                tag=tag,

                operation="WRITE",

                old_value=str(old_value),

                new_value=str(value),

            )



            return {

                "success": True,

                "message":
                "PLC value written successfully.",

                "tag": tag.name,

                "address": tag.address,

                "value": value,

            }



        except Exception as e:


            return {

                "success": False,

                "message": str(e),

            }



    @staticmethod
    def float_to_words(value):


        import struct


        data = struct.pack(

            "<f",

            value

        )


        return list(

            struct.unpack(

                "<HH",

                data

            )

        )