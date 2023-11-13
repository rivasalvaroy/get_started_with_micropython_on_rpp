'''
CHALLENGE: CAN YOU IMPROVE IT?
# ./images_breadboard/05_breadboard.png

1. Can you change the program to give the pedestrian longer to cross?
2. Can you find information about other countries’ traffic light patterns
and reprogram your lights to match?
3. Can you add a second button, so the pedestrian on the other side of the road
can signal they want to cross too?
'''

# 2
import machine
import utime
import _thread

led_red = machine.Pin(15, machine.Pin.OUT)
led_amber = machine.Pin(14, machine.Pin.OUT)
led_green = machine.Pin(13, machine.Pin.OUT)

led_green.value(0)
led_amber.value(0)
led_red.value(0)

while True:
    led_green.value(1)
    utime.sleep(5)
    led_green.value(0)
    led_amber.value(1)
    utime.sleep(2)
    led_red.value(1)
    led_amber.value(0)
    utime.sleep(5)
    led_red.value(0)
