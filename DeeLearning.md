## 深度學習
#### 參考
* [深智 DM2145](https://github.com/mc6666/DL_Book)
* [MOOC 課程](https://github.com/jumbokh/Deep-Learning-MOOC)
* [Raspberry Pi Swap Size](https://cloudolife.com/2021/01/01/Raspberry-Pi/Resizing-or-disable-Swap-Size/)
* [使用Haar Cascade 進行人臉識別](https://blog.csdn.net/wutao1530663/article/details/78294349) 
* [opencv Cascade Classifier Training](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html)
* [Haar Train](https://github.com/jumbokh/cv_face/tree/master/opencv/day3)
* [haarcascades](https://github.com/opencv/opencv/tree/master/data/haarcascades)
##
#### 程式
* [用 CNN 做圖形辨識](https://github.com/jumbokh/FSSH-class/blob/main/src/02-1.%20%E7%94%A8CNN%E5%9C%96%E5%BD%A2%E8%BE%A8%E8%AD%98%EF%BC%88%E9%82%84%E6%98%AFMNIST%EF%BC%89.ipynb)
* [Donkey Car Training  modified using Google Colab](https://colab.research.google.com/github/jumbokh/FSSH-class/blob/main/src/2020-03-01-TrainDonkeyCar.ipynb)
* [Donkey_Car_Training_using_Google_Colab](https://github.com/jumbokh/FSSH-class/blob/main/src/Donkey_Car_Training_using_Google_Colab.ipynb)

##
#### PPT
* [一天搞懂深度學習 -- 台大 李宏毅](https://github.com/jumbokh/FSSH-class/blob/main/docs/%E6%9D%8E%E5%AE%8F%E6%AF%85-%E4%B8%80%E5%A4%A9%E6%90%9E%E6%87%82%E6%B7%B1%E5%BA%A6%E5%AD%B8%E7%BF%92.pdf)
* [二元分類](https://github.com/jumbokh/FSSH-class/blob/main/docs/%E4%BA%8C%E5%85%83%E5%88%86%E9%A1%9E.ppt)
* [introduction-to-donkeycar-project](https://github.com/jumbokh/FSSH-class/blob/main/docs/introduction-to-donkeycar-project-190923012221%20(1).pdf)
##
#### 自主駕車訓練
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
