# ./images_breadboard/07_breadboard.png
import machine
import utime
import urandom

pressed = False
led = machine.Pin(15, machine.Pin.OUT)
left_button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
right_button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)


def button_handler(pin):
    global pressed
    if not pressed:
        pressed = True
        timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)
        print(f"Your reaction time was {timer_reaction} milliseconds!")


led.value(1)
utime.sleep(urandom.uniform(5, 10))
led.value(0)
timer_start = utime.ticks_ms()
left_button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)
right_button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)
