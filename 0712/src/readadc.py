import machine
import utime

adc_light = machine.ADC(machine.Pin(26))

while True:
    light = adc_light.read_u16()
	print(light)
	utime.sleep(1)