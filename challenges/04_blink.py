'''
CHALLENGE: LONGER LIGHT-UP
# ./images_breadboard/01_breadboard.png

1. How would you change your program to make the LED stay on for longer? 
2. What about staying off for longer? 
3. What’s the smallest delay you can use while still seeing the LED switch on and off?
'''

import machine
import utime

# for RPP  (the on-board LED)
# led_onboard = machine.Pin(25, machine.Pin.OUT)
# for RPP W (the on-board LED)
led_onboard = machine.Pin("LED", machine.Pin.OUT)

while True:
    led_onboard.value(1)
    utime.sleep(5)  # 1 changing 5 to a larger number (seconds)
    led_onboard.value(0)
    utime.sleep(5)  # 2 changing 5 to a larger number (seconds)

# 3
''' 
utime.sleep()
sleep for the given number of seconds, seconds can be a floating-point number to sleep
for a fractional number of seconds. Note that other MicroPython ports may not accept 
floating-point argument, for compatibility with them use sleep_ms() and sleep_us() functions.

utime.sleep_ms() delay for given number of milliseconds, should be positive or 0.

utime.sleep_us() delay for given number of microseconds, should be positive or 0
'''
