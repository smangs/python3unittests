import json


class Device:
    def __init__(self, name, ip_address, **kwargs):
        """
        :param name:
        :param ip_address:
        :param kwargs: possible keyword values are: 'mac_address',
        """
        self.name = name
        self.ip_address = ip_address
        # anything below is optional
        if 'mac_address' in kwargs:
            self.mac_address = kwargs.get('mac_address')

    def __repr__(self):
        str_items = "\"" + self.name + "\", \"" + self.ip_address + "\""
        for attr, value in self.__dict__.items():
            if not ( attr == "name" or attr == "ip_address"):
                str_items += ", " + str(attr) + "=\"" + str(value) + "\""
        return "device.Device(" + str_items + ")"

    def to_json(self):
        return json.dumps(self.__dict__)


