import unittest
import json
from module1 import device


class TestDevice(unittest.TestCase):

    def test_device(self):
        dev1 = device.Device('imac', '172.16.16.1', mac_address='c4:b3:01:d2:d5:c9')
        self.assertEqual(dev1.name, 'imac')
        self.assertEqual(dev1.ip_address, '172.16.16.1')
        self.assertEqual(dev1.mac_address, 'c4:b3:01:d2:d5:c9')

    def test_repr(self):
        dev1 = device.Device('imac', '172.16.16.1', mac_address='c4:b3:01:d2:d5:c9')
        expected = 'device.Device("imac", "172.16.16.1", mac_address="c4:b3:01:d2:d5:c9")'
        self.assertEqual(expected, str(dev1))

    def test_json(self):
        dev1 = device.Device('imac', '172.16.16.1', mac_address='c4:b3:01:d2:d5:c9')
        expected = {"name": "imac", "ip_address": "172.16.16.1", "mac_address": "c4:b3:01:d2:d5:c9"}
        # convert json to dict in order to compare
        self.assertDictEqual(expected, json.loads(dev1.to_json()))
