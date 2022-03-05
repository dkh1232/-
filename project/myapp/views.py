from django.shortcuts import render
from django.http import HttpResponse
from .models import Flats, Students
from django.db.models import Q
import os
from django.conf import settings
from django.http import FileResponse

# Create your views here.
def index(Request):
    return HttpResponse('hello world')

def showlist1(request):
    list1 = Students.objects.all()
    list2 = Students.objects.order_by('-student_math')
    list3 = Students.objects.filter(Q(student_math__lt =60) | Q(student_chinese__lt=60) | Q(student_english__lt=60))
    return render(request, 'showlist.html', {'list1': list1, 'list2': list2, 'list3': list3})

def upfile(request):
    return render(request,'upfile.html')

def savefile(request):
    # 方法一
    # if request.method == "POST":
    #     id = request.POST.get('id')
    #     name = request.POST.get('name')
    #     number = request.POST.get('number')
    #     teacher = request.POST.get('teacher')
    #     file = request.FILES['file']
    #     flat =Flats()
    #     flat.flat_id = id
    #     flat.flat_name = name
    #     flat.flat_number = number
    #     flat.flat_teacher = teacher
    #     flat.flat_image = file
    #     flat.save()
    #     return HttpResponse('上传成功')
    # else:
    #     return HttpResponse('上传失败')
    # 方法二
    if request.method == "POST":
        id = request.POST.get('id')
        name = request.POST.get('name')
        number = request.POST.get('number')
        teacher = request.POST.get('teacher')
        flat = Flats()
        flat.flat_id = id
        flat.flat_name = name
        flat.flat_number = number
        flat.flat_teacher = teacher
        f = request.FILES.get('file')
        flat.flat_image = f.name
        flat.save()
        filepath = os.path.join(settings.MEDIA_ROOT, f.name)
        with open(filepath, 'wb') as f1:
            for part in f.chunks():
                f1.write(part)
            # f2 = f.read()
            # f1.write(f2)
        return render(request, 'showfile.html', {'filepath': filepath})

def download(request):
    filepath = request.POST.get('filepath')

    # 根据上面的路径 以读的方式获取照片
    img = open(filepath, 'rb')

    # 调用FileResponse()，将图片当作参数传入并返回response对象
    response = FileResponse(img)

    # 以附件的形式下载 文件的名称为icon.jpg
    # response['Content-Disposition'] = 'attachment; filename = icon.jpg'

    # 文件的类型为图片
    response['Content-Type'] = 'image/png'

    return response