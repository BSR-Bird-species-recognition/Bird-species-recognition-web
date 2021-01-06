
## 基于深度学习的鸟类分类识别web应用 

![](https://github.com/Nilyang404/nilyang-images/raw/master/img/Typoraimage-20201121142707466.png)

![image-20210105065018663](https://i.loli.net/2021/01/05/3IQvrb4wiWkAU9z.png)

### 技术栈
前端:Bootstrap,Jquery
后端:Django
模型:VGG16
微信小程序:colorUI+wepy



### 使用方式:



后端python程序中包含bird_predict.py文件

```python
#载入tensorflow,keras环境依赖
import numpy as np
#Keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image
```



```python
#载入权重文件
MODEL_PATH = 'birds.h5'
model = load_model(MODEL_PATH,compile=False)
```



```ptyhon
model_predict(img_path, model)
#返回传入图片所属的分类
```
![](https://img2020.cnblogs.com/blog/1047378/202101/1047378-20210106082044612-772080763.png)
![](https://img2020.cnblogs.com/blog/1047378/202101/1047378-20210106082059027-1819358729.png)
![](https://img2020.cnblogs.com/blog/1047378/202101/1047378-20210106082119014-1166510485.png)
![](https://img2020.cnblogs.com/blog/1047378/202101/1047378-20210106082136720-1450452501.png)
![](https://img2020.cnblogs.com/blog/1047378/202101/1047378-20210106082153057-2034200718.png)
![](https://img2020.cnblogs.com/blog/1047378/202101/1047378-20210106082216949-211224242.png)
![](https://img2020.cnblogs.com/blog/1047378/202101/1047378-20210106082231644-1518359613.png)




### 工作示意图
![](https://img2020.cnblogs.com/blog/1047378/202101/1047378-20210106082605841-736413053.png)
![](https://img2020.cnblogs.com/blog/1047378/202101/1047378-20210106082655052-881964060.png)


