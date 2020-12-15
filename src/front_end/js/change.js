var initCropper = function (img, input){
    var $image = img;
    var options = {
        aspectRatio: 1, // 纵横比
        viewMode: 2,
        preview: '.img-preview' // 预览图的class名
    };
    $image.cropper(options);
    var $inputImage = input;
    var uploadedImageURL;
    if (URL) {
        // 给input添加监听
        $inputImage.change(function () {
            var files = this.files;
            var file;
            if (!$image.data('cropper')) {
                return;
            }
            if (files && files.length) {
                file = files[0];
                // 判断是否是图像文件
                if (/^image\/\w+$/.test(file.type)) {
                    // 如果URL已存在就先释放
                    if (uploadedImageURL) {
                        URL.revokeObjectURL(uploadedImageURL);
                    }
                    uploadedImageURL = URL.createObjectURL(file);
                    // 销毁cropper后更改src属性再重新创建cropper
                    $image.cropper('destroy').attr('src', uploadedImageURL).cropper(options);
                    $inputImage.val('');
                } else {
                  window.alert('请选择一个图像文件！');
              }
          }
      });
    } else {
        $inputImage.prop('disabled', true).addClass('disabled');
    }
}
var crop = function(){
    var $image = $('#showImg');
    var $target = $('#result');
    $image.cropper('getCroppedCanvas',{
        width:300, // 裁剪后的长宽
        height:300
    }).toBlob(function(blob){
        // 裁剪后将图片放到指定标签
        $target.attr('src', URL.createObjectURL(blob));

        

    });
}
$(function(){
    initCropper($('#showImg'),$('#input'));
});