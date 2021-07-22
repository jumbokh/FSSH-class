### JetRacer pro kit Installation
* Install python 3.7: $ sudo apt install python3.7-dev
* 設定系統 default python 版本
<pre>
jetson@jetson-desktop:~$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
update-alternatives: using /usr/bin/python2.7 to provide /usr/bin/python (python) in auto mode
jetson@jetson-desktop:~$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2
update-alternatives: using /usr/bin/python3.6 to provide /usr/bin/python (python) in auto mode
jetson@jetson-desktop:~$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 3
update-alternatives: using /usr/bin/python3.7 to provide /usr/bin/python (python) in auto mode
jetson@jetson-desktop:~$ sudo update-alternatives --config python
There are 3 choices for the alternative python (providing /usr/bin/python).

  Selection    Path                Priority   Status
------------------------------------------------------------
* 0            /usr/bin/python3.7   3         auto mode
  1            /usr/bin/python2.7   1         manual mode
  2            /usr/bin/python3.6   2         manual mode
  3            /usr/bin/python3.7   3         manual mode

Press <enter> to keep the current choice[*], or type selection number: 3
</pre>
* 安裝 cv2 時遇到 core dump, 解決方法: pip install numpy==1.19.4
### 參考
* [系統安裝](https://asahinow.blogspot.com/2019/08/nvidia-jetson-nano-tensorflow.html)
