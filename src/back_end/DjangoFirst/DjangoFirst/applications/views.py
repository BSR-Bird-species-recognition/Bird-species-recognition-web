import os
import json
from django.shortcuts import render

from django.http import HttpResponse

# 待完善
def analysisPic(File):

    return 'This is an albatross!'

# 待完善
def searchInDatabase(anaResult):

    return '很好看的鸟'

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

            # 以下为用于返回的json数据体
            data = {
                'name':anaResult,
                'descripiton':searchInDatabase(anaResult)
            }
            # 返回json
            content = json.dumps(data)
            return HttpResponse(content, content_type='application/json')
    else:
        return HttpResponse("请求方式不是post")
