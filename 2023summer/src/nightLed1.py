import machine
import utime

led_onboard = machine.Pin(1, machine.Pin.OUT)
adc_light = machine.ADC(machine.Pin(26))
treath=60000
while True:
    light = adc_light.read_u16()
	#print(light)
    if light< treath:
      led_onboard.value(1) 
      utime.sleep(0.5)
    else:
      led_onboard.value(0) 
      utime.sleep(0.5)