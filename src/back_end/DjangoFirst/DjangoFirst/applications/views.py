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
    if request.method == 'POST':
        # 获取上传的文件，如果没有文件，则默认为none
        # 注意！此处的birdPic必须与表单中提交的文件名称一致
        # File = request.FILES.get('file', None)
        File = request.body

        #File
        if File is None:
            return HttpResponse("没有上传文件")
        else:
            print('拿到文件啦')
            # 将文件传入处理函数，得到结果
            anaResult = analysisPic(File)

            # 以下为用于返回的json数据体
            data = {
                'name': anaResult,
                'descripiton': searchInDatabase(anaResult),
                # 'picture':
            }
            # 返回json
            content = json.dumps(data)
            return HttpResponse(content, content_type='application/json')
    else:
        return HttpResponse("请求方式不是post")