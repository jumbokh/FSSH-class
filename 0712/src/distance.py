from machine import Pin, time_pulse_us
import time

SOUND_SPEED=340 # 聲音在空氣中的傳播速度
TRIG_PULSE_DURATION_US=10

trig_pin = Pin(15, Pin.OUT) # 
echo_pin = Pin(14, Pin.IN)  # 

while True:
    # 準備信號
    trig_pin.value(0)
    time.sleep_us(5)
    # 產生 10 µs 脈衝
    trig_pin.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    trig_pin.value(0)

    ultrason_duration = time_pulse_us(echo_pin, 1, 30000) # 返回波的傳播時間（以微秒為單位）
    distance_cm = SOUND_SPEED * ultrason_duration / 20000

    print(f"Distance : {distance_cm} cm")
    time.sleep_ms(500)