# ./images_breadboard/03_breadboard.png
import machine
import utime

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

print(button.value())
