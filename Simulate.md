### Donkey Simulator
#### Software Download: [Donkey Gym Release](https://github.com/tawnkramer/gym-donkeycar/releases)
* [Race Edition v22.05.30](https://github.com/tawnkramer/gym-donkeycar/releases/download/v22.05.30/DonkeySimLinux.zip)
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
