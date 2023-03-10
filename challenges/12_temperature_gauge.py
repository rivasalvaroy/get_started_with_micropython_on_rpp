'''
CHALLENGE: CUSTOMISATION
# ./imgs/09_breadboard.png

1. Can you combine your two programs, and have the LED’s brightness 
controlled by the temperature reading from the on-board temperature sensor? 
2. Can you remember how many analogue inputs your Pico has? 
3. What about PWM outputs? 
4. Try adding another analogue sensor to your Pico – something like a 
light-dependent resistor (LDR), gas sensor, or barometer – and have your program read 
that instead of the potentiometer.
'''

import machine
import utime

# 1
sensor_temp = machine.ADC(4)
ldr_sensor = machine.ADC(26)
led = machine.PWM(machine.Pin(15))
led.freq(1000)
conversion_factor = 3.3 / (65535)


while True:
    led.duty_u16(sensor_temp.read_u16())
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    voltage = ldr_sensor.read_u16() * conversion_factor
    print(voltage)
    utime.sleep(2)

# 2
'''
It has three channels brought out to the GPIO pins: GP26, GP27, and GP28,
which are also known as GP26_ADC0, GP27_ADC1, and GP28_ADC2 for analogue 
channels 0, 1, and 2. There’s also a fourth ADC channel, which is connected 
to a temperature sensor built into RP2040
'''
# 3
'''
Every GPIO pin on your Pico is capable of pulse-width modulation, but the 
microcontroller’s pulse-width modulation block is made up of eight slices, 
each with two outputs.
-> making sure to only connect to pins with a letter and number combination 
you haven’t already used.
'''
