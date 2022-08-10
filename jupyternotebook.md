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
