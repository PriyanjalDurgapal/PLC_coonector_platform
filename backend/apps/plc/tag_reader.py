import struct

from .connection_service import plc_connection
from .models import PLCTagValue



class PLCTagReader:


    @staticmethod
    def read_tag(tag):

        """
        Read single PLC tag value
        """


        # Check PLC connection

        if not plc_connection.is_connected(
            tag.plc.id
        ):

            return {

                "success": False,

                "message": "PLC is not connected."

            }



        try:

            client = plc_connection.client



            value = None



            # =================================
            # BOOL
            # =================================

            if tag.data_type == "BOOL":

                result = client.batchread_bitunits(
                    tag.address,
                    1,
                )

                value = result[0]



            # =================================
            # INT / WORD
            # =================================

            elif tag.data_type in [
                "INT",
                "WORD",
            ]:


                result = client.batchread_wordunits(

                    tag.address,

                    1,

                )


                value = result[0]



            # =================================
            # REAL / FLOAT
            # =================================

            elif tag.data_type in [
                "REAL",
                "FLOAT",
            ]:


                words = client.batchread_wordunits(

                    tag.address,

                    2,

                )


                value = PLCTagReader.words_to_float(
                    words
                )



            # =================================
            # STRING
            # =================================

            elif tag.data_type == "STRING":


                result = client.batchread_wordunits(

                    tag.address,

                    10,

                )


                value = PLCTagReader.words_to_string(
                    result
                )



            else:


                return {

                    "success": False,

                    "message":
                    f"Unsupported data type {tag.data_type}"

                }



            # Save current value

            PLCTagValue.objects.update_or_create(

                tag=tag,

                defaults={

                    "value": str(value),

                    "quality": "GOOD",

                }

            )



            return {

                "success": True,

                "tag": tag.name,

                "address": tag.address,

                "data_type": tag.data_type,

                "value": value,

            }



        except Exception as e:


            PLCTagValue.objects.update_or_create(

                tag=tag,

                defaults={

                    "quality": "BAD",

                }

            )


            return {

                "success": False,

                "message": str(e),

            }



    # =====================================
    # WORDS -> FLOAT
    # =====================================

    @staticmethod
    def words_to_float(words):


        data = struct.pack(

            "<HH",

            words[0],

            words[1],

        )


        return round(

            struct.unpack(
                "<f",
                data,
            )[0],

            3,

        )



    # =====================================
    # WORDS -> STRING
    # =====================================

    @staticmethod
    def words_to_string(words):


        chars = []


        for word in words:


            low = word & 0xFF

            high = (word >> 8) & 0xFF


            if low:
                chars.append(
                    chr(low)
                )


            if high:
                chars.append(
                    chr(high)
                )



        return "".join(chars)