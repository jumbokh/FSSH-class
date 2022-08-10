## Jupyter Notebook and Jupyter Lab Install
* #### 安裝 jupyter notebook 
<pre>
sudo pip3 install jupyter
</pre>
* #### 讓 jupyter-notebook Server 可從windows連入
<pre>
jupyter notebook --generate-config
</pre>
* #### 修改 config
<pre>
修改 ~/.jupyter/jupyter_notebook_config.py 找到
#c.NotebookApp.ip = ‘localhost'
改成
c.NotebookApp.ip = '0.0.0.0’ 
</pre>
* #### 設定瀏覽器登入 jupyter notebook server密碼
<pre>
jupyter notebook password
</pre>
* #### 啓動jupyter-notebook 
<pre>
sudo jupyter-notebook --allow-root --no-browser
</pre>
##
### Jupyter Lab 安裝
<pre>
$ sudo apt-get update
$ sudo apt-get install python3-pip
$ sudo pip3 install setuptools
$ sudo apt install libffi-dev
$ sudo pip3 install cffi
$ pip3 install jupyterlab
$ mkdir ~/notebooks
</pre>
### Setup Jupyter lab as a service
#### Run below command to locate your jupyter lab binary:
<pre>
$ which jupyter-lab
/home/pi/.local/bin/jupyter-lab
</pre>
#### Create a file /etc/systemd/system/jupyter.service
<pre>
$ sudo nano /etc/systemd/system/jupyter.service
#=============== 檔案內容 ==============
[Unit]
Description=Jupyter Lab
[Service]
Type=simple
PIDFile=/run/jupyter.pid
ExecStart=/bin/bash -c "/home/pi/.local/bin/jupyter-lab --ip="0.0.0.0" --no-browser --notebook-dir=/home/pi/notebooks"
User=pi
Group=pi
WorkingDirectory=/home/pi/notebooks
Restart=always
RestartSec=10
[Install]
WantedBy=multi-user.target
</pre>
##
#### 安裝服務
<pre>
$ sudo systemctl enable jupyter.service
$ sudo systemctl daemon-reload
$ sudo systemctl start jupyter.service
# check status
$ sudo systemctl status jupyter.service
</pre>
