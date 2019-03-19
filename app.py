from module1 import device

dev1 = device.Device("mac", "10.32.32.1", mac_address="c4:b3:01:d2:d5:c9")
print(str(dev1))
dev2 = eval(str(dev1))
print(dev2.to_json())