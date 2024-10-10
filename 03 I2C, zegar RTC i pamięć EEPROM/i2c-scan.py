from machine import Pin, I2C

i2c = I2C(0, scl=Pin(1), sda=Pin(2), freq=100000)
devices = i2c.scan()

print("Found devices:")
for item in devices:
    print(f"- {item:02X}")

