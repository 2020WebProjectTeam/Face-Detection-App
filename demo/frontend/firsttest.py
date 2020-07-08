import base64

from aip import AipFace
def fun(filePath):
    """ 你的 APPID AK SK """
    APP_ID = '21132462'
    API_KEY = 'kwWpx7uiqsG7lVPKzutgdtjS'
    SECRET_KEY = 'mH8CARtgLg9jDIGBuCL3GImI69qp6LQS'

    client = AipFace(APP_ID, API_KEY, SECRET_KEY)

    # image = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1593951037794&di=ba51fc08ce9f2d1976874b124a7d4c15&imgtype=0&src=http%3A%2F%2Fimg.mp.itc.cn%2Fupload%2F20170509%2Faa320846bc7e4a6f86e1d856583f1bf5_th.jpg"

    # imageType = "URL"
    #filepath = "C:\\Users\\dell\\Pictures\\Saved Pictures\\xjq.jpg"
    with open(filePath, "rb") as fp:
        base64_data = base64.b64encode(fp.read())
        image = str(base64_data, 'utf-8')
    imageType = "BASE64"

    """ 调用人脸检测 """
    client.detect(image, imageType);

    """ 如果有可选参数 """
    options = {}
    options["face_field"] = "age,beauty,expression,face_shape,glasses,gender"
    options["max_face_num"] = 1
    options["face_type"] = "LIVE"
    options["liveness_control"] = "LOW"

    """ 带参数调用人脸检测 """
    a = client.detect(image, imageType, options)
    ans = []
    if a['error_code'] !=0:
        # print("识别失败")
        ans.append("识别失败")
    else:
        ans.append('识别的年龄为:'+str(a['result']['face_list'][0]['age'])+'岁')

        #print('识别的年龄为:'+str(a['result']['face_list'][0]['age']))
        #print('颜值打分为:'+str(a['result']['face_list'][0]['beauty']))
        if a['result']['face_list'][0]['expression']['type'] == 'none':
            exp = '不笑'
        elif a['result']['face_list'][0]['expression']['type'] == 'smile':
            exp = '微笑'
        else:
            exp = '大笑'
        ans.append('识别的表情为:'+exp)
       # print('识别的表情为:'+exp)
        if a['result']['face_list'][0]['gender']['type'] == 'male':
            rec_gender = '男性'
        else:
            rec_gender = '女性'
        ans.append('识别的性别为:'+rec_gender)
        #print('识别的性别为:'+rec_gender)
        if a['result']['face_list'][0]['glasses']['type'] == 'none':
            rec_glasses = '否'
        else:
            rec_glasses = '是'
        ans.append('是否佩戴眼镜:'+rec_glasses)
        ans.append('颜值打分为:'+str(a['result']['face_list'][0]['beauty'])+'分')
        #print('是否佩戴眼镜:'+rec_glasses)
        #print(a)
    return ans

