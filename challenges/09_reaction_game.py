'''
CHALLENGE: CUSTOMISATION
# ./images_breadboard/06_breadboard.png

1. Can you tweak your game so that the LED stays lit for a longer time? 
2. What about staying lit for a shorter time? 
3. Can you personalise the message that prints to the Shell area, 
and add a second message congratulating the player?
'''

import machine
import utime
import urandom

pressed = False
led = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)


def button_handler(pin):
    global pressed
    if not pressed:
        pressed = True
        timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)
        print("\nYour reaction time was {} milliseconds! ⚡".format(timer_reaction))
        print("That's amazing, congratulations!")  # 3


led.value(1)
utime.sleep(urandom.uniform(10, 20))    # 1
# 2
# utime.sleep(urandom.uniform(1, 5))
led.value(0)
timer_start = utime.ticks_ms()
button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)
