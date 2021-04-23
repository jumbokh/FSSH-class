# FSSH-class: [微雪官網](https://www.waveshare.net/wiki/PiRacer_Pro_AI_Kit)
## [資料連結](https://drive.google.com/drive/folders/16iQKtnFYjngqqkkFbVzOkc8HuU0624xz?usp=sharing)
### 課程時間: 4/24, 5/1, 5/8, 5/22 (星期六) 9:00~12:10
##
* ![Pirace pro AI kit](https://github.com/jumbokh/FSSH-class/blob/main/images/PiRacer-Pro-AI-Kit-details-1.jpg)
* ![xbox搖桿](https://github.com/jumbokh/FSSH-class/blob/main/images/xbox-1.JPG)
* ![樹莓派4b](https://github.com/jumbokh/FSSH-class/blob/main/images/rpi4.JPG)
### [官網教材](https://www.waveshare.net/wiki/PiRacer_Pro_AI_Kit)
* [DonkeyCar for PiRacer Pro 教程一、Raspberry Pi安装](https://www.waveshare.net/wiki/DonkeyCar_for_PiRacer_Pro_%E6%95%99%E7%A8%8B%E4%B8%80%E3%80%81Raspberry_Pi%E5%AE%89%E8%A3%85)
    * [燒錄及初步設定樹莓派](https://github.com/jumbokh/FSSH-class/blob/main/docs/Rpi-Headless.pptx)
* [DonkeyCar for PiRacer Pro 教程二、Linux PC安装](https://www.waveshare.net/wiki/DonkeyCar_for_PiRacer_Pro_%E6%95%99%E7%A8%8B%E4%BA%8C%E3%80%81Linux_PC%E5%AE%89%E8%A3%85)
* [DonkeyCar for PiRacer Pro 教程三、WEB控制](https://www.waveshare.net/wiki/DonkeyCar_for_PiRacer_Pro_%E6%95%99%E7%A8%8B%E4%B8%89%E3%80%81WEB%E6%8E%A7%E5%88%B6)
* [DonkeyCar for PiRacer Pro 教程四、校准DonkeyCar](https://www.waveshare.net/wiki/DonkeyCar_for_PiRacer_Pro_%E6%95%99%E7%A8%8B%E5%9B%9B%E3%80%81%E6%A0%A1%E5%87%86DonkeyCar)
* [DonkeyCar for PiRacer Pro 教程五、游戏杆控制](https://www.waveshare.net/wiki/DonkeyCar_for_PiRacer_Pro_%E6%95%99%E7%A8%8B%E4%BA%94%E3%80%81%E6%B8%B8%E6%88%8F%E6%9D%86%E6%8E%A7%E5%88%B6)
* [DonkeyCar for PiRacer Pro 教程六、数据采集](https://www.waveshare.net/wiki/DonkeyCar_for_PiRacer_Pro_%E6%95%99%E7%A8%8B%E5%85%AD%E3%80%81%E6%95%B0%E6%8D%AE%E9%87%87%E9%9B%86)
* [DonkeyCar for PiRacer Pro 教程七、训练数据](https://www.waveshare.net/wiki/DonkeyCar_for_PiRacer_Pro_%E6%95%99%E7%A8%8B%E4%B8%83%E3%80%81%E8%AE%AD%E7%BB%83%E6%95%B0%E6%8D%AE)
* [DonkeyCar for PiRacer Pro 教程八、自主巡线驾驶](https://www.waveshare.net/wiki/DonkeyCar_for_PiRacer_Pro_%E6%95%99%E7%A8%8B%E5%85%AB%E3%80%81%E8%87%AA%E4%B8%BB%E5%B7%A1%E7%BA%BF%E9%A9%BE%E9%A9%B6)
##
### 韌體
* [韌體 2021/3/26 版](https://drive.google.com/file/d/1Aa8K9HLEXGwRDT_qKlzEl3OWGgNNAMNs/view?usp=sharing)
### 搖桿操控
<pre>
cd ~/mycar
python manage.py drive --js
</pre>
##
### 如果想默認啟動遊戲搖杆，不希望每次都添加--js,請修改config.py，將USE_JOYSTICK_AS_DEFAULT的值改為 True。
#### 搖桿控制
* 左側模擬搖杆 - 左右調整轉向
* 右側模擬杆 - 向前增加前進油門
* 向右拉回兩次模擬量以反轉
* 每當油門不為零時，只要您處於使用者模式，就會記錄駕駛資料！
* 選擇按鈕切換模式-“User, Local Angle, Local(angle and throttle)”
* Triangle-增加最大油門
* X-降低最大油門
* 迴圈-切換錄製（預設情況下禁用。預設情況下啟用油門自動錄製）
* dpad up-增加油門比例
* dpad down -減小油門比例
* dpad left -增加轉向比例
* dpad right -減小轉向比例
* start - 切換恒定油門。設置為最大油門（由X和Triangle修改）

#### 參考網站
* [樹莓派燒錄步驟](https://atceiling.blogspot.com/2020/03/raspberry-pi-67-sdimagersdformatter.html)
* [SD Formater](https://www.azofreeware.com/2013/12/sd-formatter-40-sd.html)
* [BalenaEtcher](https://www.balena.io/etcher/)
* [DonkeyCar Docs](https://docs.donkeycar.com/)
* [gym-donkeycar](https://github.com/tawnkramer/gym-donkeycar/releases)
* [github](https://github.com/autorope/donkeycar/blob/dev/docs/guide/simulator.md)
* [微雪 WiKi](https://www.waveshare.net/wiki/PiRacer_AI_Kit)
