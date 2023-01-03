from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from utils.index_img import index_img
from .forms import RegisterForm, UserLoginForm
from .models import UserProfile, VerifyCodeEmail
from utils.send_verify_code import send_verify_email
import hashlib  # MD5加密
from django.core.mail import send_mail


def user_register(request):
    """用户的注册"""
    if request.method == 'GET':
        # 如果是get请求方法, 则直接进入到注册页面
        return render(request, 'login.html')
    else:
        # 否则就是post请求方法, 则应该是提交数据, 用于注册
        # 拿数据放到表单里面
        register_form = RegisterForm(request.POST)
        # print(register_form)
        # 用表单来进行校验
        if register_form.is_valid():
            # 如果校验正确, 则拿数据来保存
            email = request.POST.get('email')
            password = request.POST.get('password')
            nick_name = request.POST.get('nick_name')
            # print(email, password, nick_name)
            # 查询用户表当中是否有此人
            user = UserProfile.objects.filter(username=email)
            if user:
                # 如果有, 则仍然返回该页面, 并且给出提示
                return render(request, 'login.html', {'msg': '该用户已注册'})
            else:
                # 如果没有该用户, 才能保存
                # 生成一个用户对象
                user = UserProfile()
                user.username = email
                # user.email = email
                user.set_password(password)  # 将密码加密后保存,必须使用自带2022.12.24血的教训
                # user.password = password
                # psw = hashlib.md5(password.encode()).hexdigest()
                user.nick_name = nick_name
                user.save()
                # return HttpResponse(f"邮箱   {email}已经写入数据库   昵称{nick_name}    密码{psw},密码为MD5技术加密")
                # 发送邮件
                send_verify_email(email)

                return render(request, 'wait_start.html')

        else:
            # 如果数据错误
            return render(request, 'login.html', {'register_form': register_form})


#     用户登录
def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        login_form = UserLoginForm(request.POST)
    if login_form.is_valid():
        email = request.POST.get('email')
        password = request.POST.get('password')
        # 通过django的方法来校验账号和密码
        users = authenticate(username=email, password=password)
        if users:
            user_obj = UserProfile.objects.get(username=email)
            if user_obj.is_start:  # 如果激活
                login(request, users)
                # 重定向到主页
                return redirect('/')
            else:
                # 如果没激活
                return render(request, 'login.html', {'msg': '请激活 邮件'})
        else:
            return render(request, 'login.html', {'msg': '用户名或密 码错误'})
    else:
        return render(request, 'login.html', {'login_form': login_form})


def user_active(request):
    # 拿到激活链接上的秘钥
    sign = request.GET.get('sign')
    # 如果有秘钥才进行校验
    if sign:
        # 查看校验类里是否有数据
        verify_code = VerifyCodeEmail.objects.filter(code=sign)
        # 如果有, 则将其用户激活
        if verify_code:
            # 拿到当前激活的邮箱号
            email = verify_code[0].email
            # 将用户激活
            usr_obj = UserProfile.objects.get(username=email)
            usr_obj.is_start = True
            usr_obj.save()
            # 删除当前验证类
            verify_code.delete()
            return redirect(reverse('user_login'))
    return render(request, '404.html')


def user_logout(request):
    return None


def index(request):
    context = {'Bing': index_img()}

    return render(request, 'index.html', context)


