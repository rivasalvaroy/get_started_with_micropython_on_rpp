'''
CHALLENGE: BUILDING IT UP

1. Can you modify your program so it both lights the LED and prints a status message to the Shell? 
2. What would you need to change to make the LED stay on when the button isn’t pressed and switch off when it is? 
3. Can you add more buttons and LEDs to the circuit?
'''
import machine
import utime

led_external = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
# 3
led_external_two = machine.Pin(17, machine.Pin.OUT)
button_two = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        led_external.value(1)
        print("You pressed the button!")  # 1
        utime.sleep(2)
    led_external.value(0)
# 2
# change line 15 to the following
# if button.value() == 0:
# or
# if button.value() != 1:
# 3
    if button_two.value() == 1:
        led_external_two.value(1)
        utime.sleep(2)
    led_external_two.value(0)
