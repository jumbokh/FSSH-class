from machine import Pin, I2C
import utime as time
from dht import DHT11

d = DHT11(Pin(16))
    
while True:
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    print('Humidity: {}%'.format(hum))
    print('Temperature: {}{}C'.format(temp, '\u00b0'))
    time.sleep(5)