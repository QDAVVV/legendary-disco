class IPManager:
    _instance = None

    def __init__(self):
        self.ip_address = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = IPManager()
        return cls._instance

    def set_ip_address(self, ip_address):
        self.ip_address = ip_address

    def get_ip_address(self):
        return self.ip_address
