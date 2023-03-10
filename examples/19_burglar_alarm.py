# ./imgs/08_breadboard.png
import machine
import utime

sensor_pin = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)


def pir_handler(pin):
    utime.sleep_ms(100)
    if pin.value():
        print("ALARM! Motion detected!")


sensor_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)
