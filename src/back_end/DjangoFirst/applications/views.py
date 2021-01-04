#keras
from __future__ import division, print_function

import os
import time

import keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image
from werkzeug.utils import secure_filename
'''

'''
from werkzeug.utils import secure_filename

import base64
import json
import csv
import numpy as np
from django.shortcuts import render
from django.http import HttpResponse
### 预测结果部分
'''
Todo:
1.载入权重文件
2.装载模型
3.返回预测结果
'''
def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224)) #Change to 224 224

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    x = np.expand_dims(x, axis=0)
    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!
    x = preprocess_input(x)
    #preds = model.predict(x)
    #preds = model.predict_classes(x)
    preds = np.argmax(model.predict(x), axis=-1)
    #preds=(model.predict(x) > 0.5).astype("int32")

    return preds
MODEL_PATH = 'birds.h5'
# Load your trained model
model = load_model(MODEL_PATH,compile=False)

###返回数据部分
def analysisPic(File):
    result = int(model_predict(File,model))
    return str(result)
   #return '0'

def searchInDatabase(anaResult):
    with open('static/bird_data/bird_data_uft8.csv', 'r',encoding='utf-8-sig', errors='ignore') as bird_data:
        reader = csv.reader(bird_data)
        header = next(reader) #获取数据的第一列，作为后续要转为字典的键名
        csv_reader = csv.DictReader(bird_data, fieldnames=header)
        for row in csv_reader:
            dic = {}
            for key, value in row.items():
                dic[key] = value
                #print(dic)
            if (dic['Order'] == anaResult):
                return dic
    # 若出错
    return {'Ch':'未知', 'Description':'未知'}

def upload(request):
    # 请求方法为post时，进行处理
    print("收到请求")
    if request.method == 'POST':

        bas64_data= request.POST.get("image")
        with open('image_uploaded.png', 'wb') as f:
            f.write(base64.b64decode(bas64_data))
            image_path = 'image_uploaded.png'
        #print(image_path)
        if image_path is None:
            return HttpResponse("没有上传文件")
        else:
            print('取得图片')
            # 将文件传入处理函数，得到结果
            anaResult = analysisPic(image_path)
            info = searchInDatabase(anaResult)
            # 以下为用于返回的json数据体
            data = {
                'name':info['Ch'],
                'descripiton':info['Description']
            }
            # 返回json
            print('识别结果:',data["name"])
            content = json.dumps(data)
            return HttpResponse(content, content_type='application/json')
    else:
        return HttpResponse("请求方式不是post")
'''
def upload(request):
    # 请求方法为post时，进行处理
    print("收到请求")
    if request.method == 'POST':
        File = request.body
        if File is None:
            return HttpResponse("没有上传文件")
        else:
            print('取得图片')
            # 将文件传入处理函数，得到结果
            anaResult = analysisPic(File)
            info = searchInDatabase(anaResult)
            # 以下为用于返回的json数据体
            data = {
                'name':info['Ch'],
                'descripiton':info['Description']
            }
            # 返回json
            content = json.dumps(data)
            return HttpResponse(content, content_type='application/json')
    else:
        return HttpResponse("请求方式不是post")

'''