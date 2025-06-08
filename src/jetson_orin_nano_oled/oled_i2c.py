import Jetson.GPIO as GPIO
import spidev
import time
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1107, ssd1306, sh1106

print("Initializing i2c via luma.core...")

# Adjust the port and address as needed
# will vary based on connection to jetson and the display model
# following assumes ssd1306 display connected via i2c on jetson pins 27 and 28
serial = i2c(port=1, address=0x3c)
device = ssd1306(serial, width=128, height=64, rotate=0)

print("Clearing display...")
device.clear()

def main():
    print("Drawing to display...")
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((30, 40), "Hello I2C", fill="white")
    print("Done drawing. Display should show content now. 1")
    time.sleep(5)

    device.clear()
    time.sleep(1)

    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="white")
        draw.text((30, 40), "Hello I2C", fill="black")
    print("Done drawing. Display should show content now. 2")
    time.sleep(5)

if __name__ == "__main__":
    main()
