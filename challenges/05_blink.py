'''
CHALLENGE: MULTIPLE LEDS
# ./imgs/02_breadboard.png

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
led_external = machine.Pin(15, machine.Pin.OUT)
# 3
leds_external = [machine.Pin(i, machine.Pin.OUT) for i in (12, 13, 14)]

while True:
    # 1
    for i in range(3):
        led_onboard.value(1)
        led_external.value(1)
        utime.sleep(2)
        led_onboard.value(0)
        led_external.value(0)
        utime.sleep(2)
    # 2
    for i in range(3):
        led_onboard.value(1)
        led_external.value(0)
        utime.sleep(2)
        led_onboard.value(0)
        led_external.value(1)
        utime.sleep(2)

    led_onboard.value(0)
    led_external.value(0)

    # 3
    # GP 12, 13, 14
    for i in range(3):
        leds_external[0].value(1)  # GP12
        leds_external[1].value(1)  # GP13
        leds_external[2].value(1)  # GP14
        utime.sleep(2)
        leds_external[0].value(0)  # GP12
        leds_external[1].value(0)  # GP13
        leds_external[2].value(0)  # GP14
        utime.sleep(2)
