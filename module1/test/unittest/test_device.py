import unittest
from module1 import device


class TestDevice(unittest.TestCase):

    def test_device(self):
        dev1 = device.Device('imac', '172.16.16.1')
        self.assertEqual(dev1.name, 'imac')
        self.assertEqual(dev1.ip, '172.16.16.1')
