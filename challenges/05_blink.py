'''
CHALLENGE: MULTIPLE LEDS
# ./images_breadboard/02_breadboard.png

1. Can you modify the program to light up both the on-board and 
external LEDs at the same time? 
2. Can you write a program which lights up the on-board LED when 
the external LED is switched off, and vice versa? 
3. Can you extend the circuit to include more than one external LED? 
Remember, you’ll need a current-limiting resistor for every LED you use!
'''

import machine
import utime

# for RPP  (the on-board LED)
# led_onboard = machine.Pin(25, machine.Pin.OUT)
# for RPP W (the on-board LED)
led_onboard = machine.Pin("LED", machine.Pin.OUT)
led_external_one = machine.Pin(14, machine.Pin.OUT)  # 3
led_external_two = machine.Pin(15, machine.Pin.OUT)  # 3

while True:
    led_onboard.value(1)    # 1 & 2
    led_external_one.value(1)   # 1
    led_external_two.value(0)   # 2
    utime.sleep(1)
    led_onboard.value(0)
    led_external_one.value(0)
    led_external_two.value(1)
    utime.sleep(1)
