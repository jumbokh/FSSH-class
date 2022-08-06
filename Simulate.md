### Donkey Simulator
#### Software Download: [Donkey Gym Release](https://github.com/tawnkramer/gym-donkeycar/releases)
* [Race Edition v22.05.30](https://github.com/tawnkramer/gym-donkeycar/releases/download/v22.05.30/DonkeySimLinux.zip)
##### put at: ~/projects/DonkeySimLinux
<pre>
cd ~/projects
wget https://github.com/tawnkramer/gym-donkeycar/releases/download/v22.05.30/DonkeySimLinux.zip
unzip DonkeySimLinux.zip
</pre>
##
#### Setup
<pre>
cd ~/projects
git clone https://github.com/tawnkramer/gym-donkeycar
cd gym-donkeycar
conda activate donkey
pip install -e .[gym-donkeycar]
</pre>
#### Edit myconfig.py
<pre>
DONKEY_GYM = True
DONKEY_SIM_PATH = "/home/<user-name>/projects/DonkeySimLinux/donkey_sim.x86_64"
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
