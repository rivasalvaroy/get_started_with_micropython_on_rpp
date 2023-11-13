'''
CHALLENGE: CAN YOU IMPROVE IT?
# ./images_breadboard/04_breadboard.png

1. Can you change the program to give the pedestrian longer to cross? 
2. Can you find information about other countries’ traffic light patterns 
and reprogram your lights to match? -> next program 08_traffic_lights.py
3. Can you add a second button, so the pedestrian on the other side of the road 
can signal they want to cross too?
'''

import machine
import utime
import _thread

led_red = machine.Pin(15, machine.Pin.OUT)
led_amber = machine.Pin(14, machine.Pin.OUT)
led_green = machine.Pin(13, machine.Pin.OUT)
button_side_a = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)  # 3
button_side_b = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)  # 3
buzzer = machine.Pin(12, machine.Pin.OUT)

global button_pressed
button_pressed = False


def button_reader_thread():
    global button_pressed
    while True:
        if button_side_a.value() == 1 or button_side_b.value() == 1:    # 3
            button_pressed = True
        utime.sleep(0.01)


_thread.start_new_thread(button_reader_thread, ())

while True:
    if button_pressed == True:
        led_red.value(1)
        for i in range(20):  # 1
            buzzer.value(1)
            utime.sleep(0.2)
            buzzer.value(0)
            utime.sleep(0.2)
        button_pressed = False
    led_red.value(1)
    utime.sleep(5)
    led_amber.value(1)
    utime.sleep(2)
    led_red.value(0)
    led_amber.value(0)
    led_green.value(1)
    utime.sleep(5)
    led_green.value(0)
    led_amber.value(1)
    utime.sleep(5)
    led_amber.value(0)
