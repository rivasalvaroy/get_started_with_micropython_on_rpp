'''
CHALLENGE: TIMINGS
# ./images_breadboard/07_breadboard.png

1. Can you modify the messages that print? 
2. Can you add a third button, so that three people can play at once? 
3. Is there an upper limit to how many buttons you could add? 
4. Can you add the timer back into your program, so it tells the winning 
player how quick their reaction time was?
'''
import machine
import utime
import urandom

pressed = False
led = machine.Pin(15, machine.Pin.OUT)
left_button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
middle_button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
right_button = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)   # 2
fastest_button = None
timer_reaction = None


def button_handler(pin):
    global timer_reaction   # 4
    timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)    # 4
    global pressed
    if not pressed:
        pressed = True
        global fastest_button
        fastest_button = pin


led.value(1)
utime.sleep(urandom.uniform(5, 10))
led.value(0)
timer_start = utime.ticks_ms()  # 4
left_button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)
middle_button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)
right_button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)

while fastest_button is None:
    utime.sleep(1)
if fastest_button is left_button:
    print("The player on the left wins!")   # 1
elif fastest_button is middle_button:
    print("The player in the middle wins!")  # 1
elif fastest_button is right_button:
    print("The player on the right wins!")  # 1 2
print(f"Your reaction time was {timer_reaction} milliseconds!")  # 4

# 3
'''
All GPIO pins on the board can be configured as an external interrupt 
if one of the following changes in the state of GPIO pins occur:

    Level high(+3v)
    Level Low(GND)
    Positive edge (transition from active low to active high)
    Negative edge (transition from active high to active low)
'''
