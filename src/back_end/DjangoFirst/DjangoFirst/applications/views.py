import os
import json
import csv
from django.shortcuts import render

from django.http import HttpResponse

# 待完善
def analysisPic(File):

    return '55'

def searchInDatabase(anaResult):
    with open('static/bird_data/bird_data_uft8.csv', 'r',encoding='utf-8-sig', errors='ignore') as bird_data:
        reader = csv.reader(bird_data)
        header = next(reader) #获取数据的第一列，作为后续要转为字典的键名
        csv_reader = csv.DictReader(bird_data, fieldnames=header)
        for row in csv_reader:
            dic = {}
            for key, value in row.items():
                dic[key] = value
                print(dic)
            if (dic['Order'] == anaResult):
                return dic
    # 若出错
    return {'Ch':'未知', 'Description':'未知'}

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
