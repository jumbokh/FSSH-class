import machine
import utime

adc_light = machine.ADC(machine.Pin(26))
pwm = machine.PWM(machine.Pin(15))
pwm.freq(1000)

while True:
    light = adc_light.read_u16()
	pwm.duty_u16(light)
	print(light)
	utime.sleep(1)