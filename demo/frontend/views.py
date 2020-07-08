from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
import base64
import os
import uuid
from .firsttest import fun

def index(request):
    return render(request, 'frontend/index.html')

def picupload(request):
    if request.POST:
        obj = request.FILES.get('image', None)
        print(type(obj))
        # 文件名
        picFileName = obj.name
        # 文件大小
        picFileSize = obj.size
        # 文件后缀
        picFileStuff = os.path.splitext(picFileName)[1]

        # [测试]
        print('文件名称: {0}'.format(picFileName))
        print('文件大小: {0}'.format(picFileSize))
        print('文件后缀: {0}'.format(picFileStuff))

        # 模拟可以上传的文件的类型列表
        allowedTypes = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

        # 判断上传文件是否受限
        if picFileStuff.lower() not in allowedTypes:
            # 需要响应到前台说一声, '文件格式不对'
            return render(request, 'picupload.html', {'error_msg':'文件格式不对'})

        # 可以生成文件的唯一标识名称
        picuploadUniqueName = str(uuid.uuid1()) + picFileStuff
        # [测试]
        print('生成的图片的唯一名称为: {0}'.format(picuploadUniqueName))

        # 设置文件上传到服务器的目录地址
        uploadPath = os.path.join(os.getcwd(), 'frontend/static/frontend/')

        if not os.path.exists(uploadPath):
            os.mkdir(uploadPath)
            print('创建上传目录成功')
        else:
            print('服务器原本就存在该目录')

        # 设置上传文件的全路径
        picFileAbsPath = uploadPath + os.sep + picuploadUniqueName
        print('上传图片的全名称: {0}'.format(picFileAbsPath))

        try:
            with open(picFileAbsPath, 'wb+') as fp:
                # 分块处理
                for chunk in obj.chunks():
                    fp.write(chunk)

                context = dict()

                a = fun(picFileAbsPath)
                # print(picFileAbsPath)
                if len(a) != 1:
                    context['success_msg'] = '上传图片成功，识别内容如下'
                    context['age'] = a[0]
                    context['expression'] = a[1]
                    context['gender'] = a[2]
                    context['glasses'] = a[3]
                    context['beauty'] = a[4]
                else:
                    context['success_msg'] = '文件上传成功，但无法识别图像内容'
                context['picurl'] = picuploadUniqueName

                return render(request, 'frontend/picupload.html', context)

        except:
            return render(request, 'frontend/picupload.html', {'error_msg':'图片上传失败'})

        return render(request, 'frontend/picupload.html')

    else:
        return render(request, 'frontend/picupload.html')


def upload(request):
    picFileAbsPath = 'app/static/file/timg.jpg'
    try:
        context = dict()
        a = fun(picFileAbsPath)
        if len(a) != 1:
            context['success_msg'] = '上传图片成功，识别内容如下'
            context['age'] = a[0]
            context['expression'] = a[1]
            context['gender'] = a[2]
            context['glasses'] = a[3]
            context['beauty'] = a[4]
        else:
            context['success_msg'] = '文件上传成功，但无法识别图像内容'
        context['picurl'] = 'timg.jpg'
        print(a)
        return render(request, 'frontend/aftercamera.html', context)
    except:
        return render(request, 'frontend/aftercamera.html', {'error_msg':'图片上传失败'})


def camera(request):
    if request.POST:
        picFileAbsPath = 'frontend/static/timg.jpg'
        image = request.POST.get('image', '')
        image2 = image.split(',')[1]
        image_data = base64.b64decode(image2)
        with open(picFileAbsPath, 'wb+') as f:
            f.write(image_data)
        return HttpResponse('')
    else:
        return render(request, 'frontend/test.html')