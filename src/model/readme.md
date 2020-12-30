#### model说明

2020/12/30

最后确定模型Vgg16,训练框架采用tensorflow,keras

训练过程在vgg16_final.ipynb中

导出权重文件:birds.h5



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



