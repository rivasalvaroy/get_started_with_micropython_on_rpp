# ./images_breadboard/01_breadboard.png
import machine
import utime

# for RPP  (the on-board LED)
# led_onboard = machine.Pin(25, machine.Pin.OUT)
# for RPP W (the on-board LED)
led_onboard = machine.Pin("LED", machine.Pin.OUT)

while True:
    led_onboard.toggle()
    utime.sleep(5)
