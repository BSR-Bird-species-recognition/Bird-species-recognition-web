const app = getApp();
Page({
  data: {
    StatusBar: app.globalData.StatusBar,
    CustomBar: app.globalData.CustomBar,
    tempFilePaths: '',
    defaultImg:'img/def.png',
    text:'',
  },
  onLoad: function () {
    if(tempFilePaths == ''){
      tempFilePaths=data.defaultImg
      this.setData({
        tempFilePaths: defaultImg       
      })
    }
  },
  errorFunction:function(e){
    if(e.type=="error"){
      var errorImgIndex = e.target.dataset.errorimg //获取错误图片循环的下标
      var tempFilePaths= this.data.tempFilePaths    　　　　　　　//将图片列表数据绑定到变量
      tempFilePaths[errorImgIndex] = this.data.defaultImg //错误图片替换为默认图片
      this.setData({
        evaluteUserPic: evaluteUserPic
      })
    }
  },
  chooseimage: function () {
    var that = this;
    that.setData({
      text:'',
      categoryName:''
    }) 

    wx.showActionSheet({
      itemList: ['从相册中选择', '拍照'],
      itemColor: "#CED63A",
      success: function (res) { 
        if (!res.cancel) {
          if (res.tapIndex == 0) {
            that.chooseWxImage('album')
          } else if (res.tapIndex == 1) {
            that.chooseWxImage('camera')
          }
        }
      }
    })
  },
  chooseWxImage: function (type) {
    var that = this;
    wx.chooseImage({
      sizeType: ['original', 'compressed'],
      sourceType: [type],
      success: function (res) { 
        wx.showLoading({
          title: '正在努力识别中',
        })
        wx.uploadFile({
          url: 'http://127.0.0.1:8000/miniupload/', //仅为示例，非真实的接口地址
          filePath: res.tempFilePaths[0],
          name: 'image',
          formData: {
            'image': 'test'
          },
          success: function (res) {           
            wx.hideLoading();
            var data = res.data
            var datas = JSON.parse(data)
            var categoryName='鸟类'
            if (datas.name != '' && datas.descripiton!=''){
              that.setData({
                name:datas.name,
                description: datas.descripiton
              });
            }
            that.setData({
              text: datas.root + '-' + datas.keyword,
              categoryName: categoryName
            }) 
          
          }
        })         
        that.setData({
          tempFilePaths: res.tempFilePaths[0]          
        })
      }
    })
  }
}) 