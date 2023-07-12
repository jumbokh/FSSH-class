from machine import Pin, ADC, PWM          #importing Pin, ADC and PWM classes
from time import sleep                                 #importing sleep class

led=PWM(Pin(16))             #GPIO13 set as pin
led.freq(1000)

potentiometer=ADC(28)             #creating potentiometer object

while True:
  potentiometer_value=potentiometer.read_u16()           #reading analog pin
  print(potentiometer_value)
  led.duty_u16(potentiometer_value)             #setting duty cycle value as that of the potentiometer value
  sleep(0.25)
