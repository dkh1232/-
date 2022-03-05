from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from django.contrib.sessions.models import Session
# Create your views here.
def index(request):
    return HttpResponse('app2')


def register(request):
    message = "注册失败"
    if request.method == "POST":
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        Email = request.POST.get('email')
        user = User()

        try:
            if User.objects.get(username=Username):
                message1 = "用户名已存在"
                return HttpResponse(message1)
        except:
            user.username = Username
        user.password = Password

        try:
            if User.objects.get(email=Email):
                message2 = "邮箱已存在"
                return HttpResponse(message2)
        except:
            user.email = Email
        user.save()
        return render(request,'success.html',{'user':user})

    return HttpResponse(message)

def login(request):
    message = "请求失败，请重新登录"
    if request.method == "GET":
        return HttpResponse(message)
    else:
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        user = User.objects.filter(username=name,password=pwd).first()
        if user:
            request.session['name']=user.username
            print(request.session['name'])
            return render(request,'index.html',{'user':user})
        else:
            return HttpResponse(message)

def logout(request):
    return HttpResponse('退出成功')