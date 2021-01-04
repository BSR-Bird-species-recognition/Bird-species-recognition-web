"""DjangoFirst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from applications import views


from django.shortcuts import HttpResponse, render, redirect
def index(request): # 此处request只是形参，可以更改为任意名称，与下方返回参数列表第一个参数相同即可
    # return HttpResponse('index') # 返回一个字符串
    return render(request,'index.html')


# def login(request):
#     return render(request,'login.html')



# 地址，函数对列表
urlpatterns = [
    path('index/',index),
    path('admin/', admin.site.urls),
    path('upload/', views.upload),
]
