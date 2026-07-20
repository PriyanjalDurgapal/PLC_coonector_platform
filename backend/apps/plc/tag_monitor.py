from .models import PLCTag
from .tag_reader import PLCTagReader



class PLCTagMonitor:


    @staticmethod
    def read_all_tags(plc_id):

        """
        Read all active tags of a PLC
        """


        tags = (
            PLCTag.objects
            .filter(
                plc_id=plc_id,
                is_active=True,
            )
            .select_related("plc")
        )


        results = []


        for tag in tags:


            result = PLCTagReader.read_tag(
                tag
            )


            results.append(
                result
            )


        return results