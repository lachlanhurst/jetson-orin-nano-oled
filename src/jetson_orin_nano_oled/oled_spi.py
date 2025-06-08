import Jetson.GPIO as GPIO
import spidev
import time
from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import sh1107, ssd1306, sh1106

# BCM pin 5 (physical pin 29 on the Jetson)
DC_PIN  = 5
# BCM pin 6 (physical pin 31 on the Jetson)
RST_PIN = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup([DC_PIN, RST_PIN], GPIO.OUT, initial=GPIO.HIGH)

# Reset the panel
GPIO.output(RST_PIN, GPIO.LOW)
time.sleep(0.1)
GPIO.output(RST_PIN, GPIO.HIGH)
time.sleep(0.1)

jspi = spidev.SpiDev()
# bus 0 (= SPI0), device 0 (= CS0)
jspi.open(0, 0)
jspi.max_speed_hz = 1000000
jspi.mode = 0

print("Initializing SPI via luma.core...")
serial = spi(port=0, device=0, spi=jspi, gpio=GPIO, gpio_DC=DC_PIN, gpio_RST=RST_PIN)
device = sh1107(serial, width=128, height=128, rotate=0)

print("Clearing display...")
device.clear()

def main():
    print("Drawing to display...")
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((30, 40), "Hello SPI", fill="white")
    print("Done drawing. Display should show content now. 1")
    time.sleep(5)

    device.clear()
    time.sleep(1)

    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="white")
        draw.text((30, 40), "Hello SPI", fill="black")
    print("Done drawing. Display should show content now. 2")
    time.sleep(5)

if __name__ == "__main__":
    main()
