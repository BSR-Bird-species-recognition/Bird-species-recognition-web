//var access_token = "24.48d56a455b50a47d2d9c488ad3ffdc6b.2592000.1609058213.282335-23054511";
    // 监听图片选择事件
    function getImg (event) {
        var imageBase = "";
        var reader = new FileReader();
        reader.readAsDataURL(event.target.files[0]);
        reader.onload = function (e) {
            imageBase = e.target.result.replace("data:image/png;base64,","");
            $("#showImg").prop("src", "data:image/png;base64," + imageBase);
            $.ajax({
                header: {
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                type: "post",
                url: "../upload/",
                async: true,
                data: {
//                    access_token: access_token,
//                    id_card_side: "front",
                    image: imageBase
                },
                dataType: "json",
                timeout: 30000,
                success: function (data) {
                    console.log("解析成功");
                    console.log(data);
                },
                error: function (xhr) {
                    console.log("请求解析失败");
                }
            });
        }
    }