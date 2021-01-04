# Bird-species-recognition-web
基于深度学习的鸟类分类识别web应用 

![](https://github.com/Nilyang404/nilyang-images/raw/master/img/Typoraimage-20201121142707466.png)

![image-20210105065018663](https://i.loli.net/2021/01/05/3IQvrb4wiWkAU9z.png)



**使用方式:**



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



