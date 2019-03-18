class Device:
    def __init__(self, name, ip_address):
        self.name = name
        self.ip = ip_address

    def __repr__(self):
        return "device.Device(\"" + self.name + "\", \"" + self.ip + "\")"

    def to_json(self):
        return {
            "name": self.name,
            "ip": self.ip,
        }


