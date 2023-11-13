'''
CHALLENGE: CUSTOMISATION
# ./images_breadboard/08_breadboard.png

1. Can you extend the burglar alarm with another PIR sensor? 
2. What about adding another LED, or another buzzer? 
3. Can you change the messages that print to match the areas you’re covering with each sensor? 
4. Can you make the buzzer sound for longer, or for less time? 
5. Can you think of any other sensors, apart from a PIR sensor, that might work well in a burglar alarm?
'''

import machine
import utime

sensor_pir = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
sensor_pir2 = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_DOWN)
sensor_pir3 = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_DOWN)    # 1
led = machine.Pin(15, machine.Pin.OUT)
buzzer = machine.Pin(14, machine.Pin.OUT)
buzzer2 = machine.Pin(13, machine.Pin.OUT)  # 2


def pir_handler(pin):
    utime.sleep_ms(100)
    if pin.value():
        if pin is sensor_pir:
            print("ALARM! Motion detected in kitchen!")  # 3
        elif pin is sensor_pir2:
            print("ALARM! Motion detected in garage!")  # 3
        elif pin is sensor_pir3:
            print("ALARM! Motion detected in stairs !")  # 3
        for i in range(100):  # 4 change value to 25 for less time
            led.toggle()
            buzzer.toggle()
            buzzer2.toggle()
            utime.sleep_ms(100)
    buzzer.value(0)  # 4
    buzzer2.value(0)    # 4


sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)
sensor_pir2.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)
sensor_pir3.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)

while True:
    led.toggle()
    utime.sleep(5)

# 5
# ultrasonic sensor
