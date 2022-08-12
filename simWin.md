### Donkey car simulator for Windows
#### 需要軟體:
* 1. python [Anaconda](https://www.anaconda.com/products/distribution)
* 2. [git command](https://git-scm.com/download/win)
* 3. donkeycar
* 4. [gym-donkeycar]()
* 5. [DonkeySimWin](https://github.com/tawnkramer/gym-donkeycar/releases/download/v22.05.30/DonkeySimWin.zip)
##
### Donkey Simulator
#### Software Download: [Donkey Gym Release](https://github.com/tawnkramer/gym-donkeycar/releases)
* [Race Edition v22.05.30](https://github.com/tawnkramer/gym-donkeycar/releases/download/v22.05.30/DonkeySimWin.zip)
##### put at: D:\projects\DonkeySimLinux
<pre>
d:
mkdir projects
cd D:\projects
</pre>
## 下載 [DonkeySim for WIndows](https://github.com/tawnkramer/gym-donkeycar/releases/download/v22.05.30/DonkeySimWin.zip)
##
#### Setup
<pre>
## 開啟 anaconda prompt
cd d:\projects
git clone https://github.com/autorope/donkeycar
cd donkeycar
git checkout master
pip install -e .
git clone https://github.com/tawnkramer/gym-donkeycar
cd gym-donkeycar
pip install -e .[gym-donkeycar]
cd D:\projects\donkeycar
donkey createcar --path=d:\mycar
</pre>
#### Edit myconfig.py
<pre>
DONKEY_GYM = True
DONKEY_SIM_PATH = "D:\DonkeySimWin\donkey_sim.exe"
DONKEY_GYM_ENV_NAME = "donkey-generated-track-v0"
</pre>
##
#### Drive
<pre>
python manage.py drive
# or
python manage.py drive --js
</pre>
##
#### Train
<pre>
donkey train --tub ./data --model models/mypilot.h5
</pre>
##
#### Test
<pre>
python manage.py drive --model models/mypilot.h5
</pre>
##
#### Sample Driving Data
* [Sample Data](https://drive.google.com/open?id=1A5sTSddFsf494UDtnvYQBaEPYX87_LMp)
##
