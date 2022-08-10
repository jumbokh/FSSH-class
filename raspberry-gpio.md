### Raspberry pi GPIO

* 在 Python 中設定GPIO.BOARD與GPIO.BCM有何不同
<pre>
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
</pre>
或者
<pre>
GPIO.setmode(GPIO.BCM)
</pre>
##
#### 這個GPIO.BOARD 選項是指定在電路版上接脚的號碼
#### 這個GPIO.BCM 選項是指定GPIO後面的號碼
#### 在撰寫程式時要先清楚你指定的數字要使用的是GPIO.BOARD或是GPIO.BCM的方式
##
### Lab
* Lab1 [Lab1_LED]()
* Lab2 [Lab2_DHT11]()
* Lab3 [Lab3 RC電路]()
* Lab4 [Lab4 光感測]()
* Lab5 [Lab5 超音波測距]()
##
