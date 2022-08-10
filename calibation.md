* left:490
* right: 390
* stop 410
* slow forward 440
* slow reverse 390
* fast forward 550
* fast reverse 310
##
* 校準
    * 方向舵
        * cd ~/mycar
        * donkey calibrate --channel 0 --bus=1
        * ![方向舵校正](https://github.com/jumbokh/FSSH-class/blob/main/images/DonkeyCar_for_Jetson_Nano_4-3.png.png)
        * ### 輸入360，此時應該看到舵機轉動，如果沒有轉動輸入400或者300試下。
        * ### 從起始值慢慢調節，使舵機轉到最中間的位置，試幾下此時的值。例如330.將此值+/- 100 將大概得到最左最右的值230和430.
        * ### 在config.py檔找到如下部分，將STEERING_LEFT_PWM和STEERING_RIGHT_PWM的值改為實際校準的值。
        * ![方向舵校正](https://github.com/jumbokh/FSSH-class/blob/main/images/DonkeyCar_for_Jetson_Nano_4-6.png.png)
     * 油門
        * cd ~/mycar
        * donkey calibrate --channel 1 --bus=1
        * ### 370 為靜止, 500 為最大油門, 220 為反向最大油門, 比照方向舵調整
     * ### 最後, 必須修改 config.py 中方向舵(STEERING) 和 油門 (throttle)的 channel 剛好相反, 必須改為:
     * ### STEERING_CHANNEL = 0
     * ### THROTTLE_CHANNEL = 1
