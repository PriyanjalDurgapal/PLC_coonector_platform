import time

import pymcprotocol


class PLCConnectionService:

    def __init__(self):

        self.client = None
        self.connected = False

        self.plc = None
        self.plc_id = None

        self.last_latency = None


    def connect(self, plc):

        try:

            # Disconnect previous PLC if connected
            if self.connected:
                self.disconnect()

            client = pymcprotocol.Type3E()

            start = time.time()

            client.connect(
                plc.ip_address,
                plc.port,
            )

            end = time.time()

            self.client = client
            self.connected = True

            self.plc = plc
            self.plc_id = plc.id

            self.last_latency = round(
                (end - start) * 1000,
                2,
            )

            return {
                "success": True,
                "message": "PLC connected successfully.",
                "latency": self.last_latency,
            }

        except Exception as e:

            self.client = None
            self.connected = False
            self.plc = None
            self.plc_id = None
            self.last_latency = None

            return {
                "success": False,
                "message": str(e),
            }


    def disconnect(self):

        try:

            if self.client:
                self.client.close()

        except Exception:
            pass

        self.client = None
        self.connected = False
        self.plc = None
        self.plc_id = None
        self.last_latency = None

        return {
            "success": True,
            "message": "PLC disconnected successfully.",
        }


    def status(self):

        return {
            "connected": self.connected,
            "latency": self.last_latency,
            "plc_id": self.plc_id,
            "plc_name": self.plc.name if self.plc else None,
        }


    def is_connected(self, plc_id):

        return (
            self.connected
            and
            self.plc_id == plc_id
        )


plc_connection = PLCConnectionService()