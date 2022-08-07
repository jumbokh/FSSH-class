# FSSH-class: 
### [DonkeyCar Trainning Tutorial](https://github.com/jumbokh/FSSH-class/blob/main/docs/DonkeyCar-Tutorial.pptx)
### [DonkeyCar](https://docs.donkeycar.com/)
### [微雪官網](https://www.waveshare.net/wiki/PiRacer_Pro_AI_Kit) [English](https://www.waveshare.com/wiki/PiRacer_Pro_AI_Kit)
### [Get Your Raspberry Pi Working](https://docs.donkeycar.com/guide/robot_sbc/setup_raspberry_pi/)
### [A self-driving RC car using Raspberry Pi](https://github.com/hamuchiwa/AutoRCCar)
### 工具下載
* [putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
* [MobaXterm](https://mobaxterm.mobatek.net/download-home-edition.html)
* [微雪 piracer-1 image(pass:wsdz)](https://pan.baidu.com/s/1xvlqA2Ct0mxiUfOzekcFaA)
* [Rasbian: buster iso](https://downloads.raspberrypi.org/raspbian_lite_latest)
    * 樹莓派系統設定:
        * 已連接wifi
        * 開啟ssh
        * 啟動I2C接口
        * 啟動相機
        * 擴展檔案系統
### 課程時間: 8/10, 8/11, 8/12, 8/15 9:00~16:00
#### 開關機, 登入登出, 執行
* 開機:
    * 檢視 oled 第一行的 ip 位置, 比如: 192.168.0.100
    * 開啟 putty, open 192.168.0.100
    * login: pi
    * password: raspberry (螢幕不會顯示,不會回應, 直接打完後<Enter>)
* 關機:
    * Ctrl-C, 回到 pi$ 提示符號
    * 打三次 sync
    * sudo shutdown -h now
    * 等到樹莓派的網路燈熄滅
    * 切換開關至 off

#### 樣本資料 [參考](https://robocaresslingen.github.io/BookDownDocu/donkeyCar.html)
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
* 自定義搖桿: [create js](https://docs.donkeycar.com/utility/donkey/#joystick-wizard)
* 執行:
    * Web 控制:
        * 登入樹莓派
        * 見到提示符號出現
        * 輸入指令:
            * cd ~/mycar
            * python manage.py drive    
            * 在電腦的瀏覽器, 輸入網址: 192.168.0.100:8887
            * 如果顯示鏡頭為倒立, 需修改 myconfig.py 之中的 CAMER_VFLIP 
            * 第 29 行, 改為
            * CAMERA_VFLIP = True
     * 遊戲搖桿控制: [使用不同的搖桿](https://docs.donkeycar.com/parts/controllers/#joystick-controller)
         * 登入至樹莓派, 步驟如上
         * 執行: 
         * python manage.py drive --js
     * [設定搖桿值](https://docs.donkeycar.com/utility/donkey/#joystick-wizard)
     * [模擬程式](https://docs.donkeycar.com/guide/simulator/)
     * [sample data](https://github.com/autorope/donkey_datasets)
     * [Mobile APP Controller](https://medium.com/robocar-store/robocar-controller-quick-start-guide-bdf8cb16d7ce)
* 訓練
     * [Train](https://github.com/jumbokh/FSSH-class/blob/main/src/Donkey_Car_Training_using_Google_Colab.ipynb)
     * [train_predict_test](https://nbviewer.org/github/jumbokh/FSSH-class/blob/main/src/train_predict_test.ipynb)
* 自駕
#### python manage.py drive --model ~/mycar/models/mypilo
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
### RC車架
* ![detail](https://github.com/jumbokh/FSSH-class/blob/main/images/PiRacer-Pro-AI-Kit-details-11.jpg)
### 越野RC車架
* ![越野](https://github.com/jumbokh/FSSH-class/blob/main/images/TB2Vpdtt3FkpuFjSspnXXb4qFXa_!!14410097.jpg)
* ![圖](https://github.com/jumbokh/FSSH-class/blob/main/images/750-7.jpg)
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
* [Samba Share](https://www.waveshare.net/study/article-1047-1.html)
* [樹莓派燒錄步驟](https://atceiling.blogspot.com/2020/03/raspberry-pi-67-sdimagersdformatter.html)
* SD卡格式化 [SD Formater](https://www.azofreeware.com/2013/12/sd-formatter-40-sd.html)
* 燒錄器 [BalenaEtcher](https://www.balena.io/etcher/)
* 官方文件 [DonkeyCar Docs](https://docs.donkeycar.com/)
* 樣本data: [sampleing dataset](https://drive.google.com/file/d/13dXSoHx6YpTvesdyUMe6o_ZfyYTYlfaK/view)
* 模擬賽車data: [Sim Dataset](https://drive.google.com/file/d/1A5sTSddFsf494UDtnvYQBaEPYX87_LMp/view)
* Youtube: [Donkey Car Assembly Video](https://www.youtube.com/watch?v=OaVqWiR2rS0&t=48s)
* [gym-donkeycar](https://github.com/tawnkramer/gym-donkeycar/releases)
* [模擬軟體]([https://github.com/autorope/donkeycar/blob/dev/docs/guide/simulator.md](https://docs.donkeycar.com/guide/simulator/))
* [微雪 WiKi](https://www.waveshare.net/wiki/PiRacer_AI_Kit)
* [Learning to Drive Smoothly in Minutes](https://towardsdatascience.com/learning-to-drive-smoothly-in-minutes-450a7cdb35f4)
* [驢車(Donkey Car)，一個基於 Raspberry Pi 與機器學習的開源無人小車專案介紹](https://www.slideshare.net/raspberrypi-tw/donkey-car-raspberry-pi?qid=21ac0c87-65e4-41ec-a987-446185fc65f0&v=&b=&from_search=4)
* Youtube: [Building Custom Self Driving Car with Donkey Car under 10 mints.](https://www.youtube.com/watch?v=J6Ll5Obtuxk)
* RC車架: [配件](https://item.taobao.com/item.htm?spm=2013.1.0.0.3f4a6ab2ngyMkn&id=553479800530)
* [舵機 E6001](https://item.taobao.com/item.htm?spm=a230r.1.14.55.5cdb726dISP3VD&id=620613325708&ns=1&abbucket=14#detail)
* [RC380強磁碳刷馬達](https://item.taobao.com/item.htm?spm=a230r.1.14.101.42445bb7AZYmQV&id=613122254964&ns=1&abbucket=14#detail)
* [轉向機](https://item.taobao.com/item.htm?id=543223247962&ali_refid=a3_430620_1006:1121604386:N:gs34vNq9Nhih8xV68YYY%2BmzNxn5UFqDD:48d194d12f815ce4483a1fa3c5447730&ali_trackid=1_48d194d12f815ce4483a1fa3c5447730&spm=a230r.1.14.1#detail)
* [Raspberry pi 4B 4G](https://item.taobao.com/item.htm?id=596761703325&ali_refid=a3_430620_1006:1110571867:N:nu18v9KpIqv%2BIEc3RDNh2bHs5uAbSgnc:3df60e4ec69bd4d780300e513d083020&ali_trackid=1_3df60e4ec69bd4d780300e513d083020&spm=a230r.1.14.1#detail)
* [越野遙控車]([https://www.pcone.com.tw/product/info/181015845171?utm_campaign=gsa&sid=gsa_4&utm_source=google&utm_medium=gsa&utm_content=4&gclid=EAIaIQobChMI7YrdnYug8AIV0-7jBx3P0A5HEAYYAyABEgLk8_D_BwE](https://shopee.tw/search?keyword=%E8%B6%8A%E9%87%8E%E9%81%99%E6%8E%A7%E8%BB%8A&utm_source=google&utm_medium=seller&utm_campaign=s104788746_SS_TW_GSHP_Roborock_PMAX&is_seller=true&gclid=Cj0KCQjwn4qWBhCvARIsAFNAMigtkuqfkNirLnBElRD5hb80eSRfc8fsKD8NLOY77oEwIVviAyuIlmQaApwNEALw_wcB))
* [3D列印車架](https://www.thingiverse.com/thing:2566276)
* [wlmodel](http://www.wlmodel.com/app/detail.html?goods_id=4)
* [自動車 -- 訓練後的驢車](https://www.youtube.com/watch?v=QwsIGYvoZro)
* [duckietown](https://github.com/duckietown)
* [Duckiebot operation manual](https://docs.duckietown.org/daffy/opmanual_duckiebot/out/index.html)
* [小鴨城](https://www.raspberrypi.com.tw/34886/official-duckiebot-db18-duckietown?fbclid=IwAR30FxO-y_cS0sUI8zkbCwjwSQ-tKZLFTksugn4lpDag9srgmGWg4ok1fjg)
* [Youtube : 小車影片收集](https://www.youtube.com/playlist?list=PL3QkiMMAl4cSiUaYW0UOKAzQ3O5zBA1Dc)
