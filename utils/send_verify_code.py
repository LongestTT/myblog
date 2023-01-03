from django.conf import settings
from django.core.mail import send_mail
import hashlib
import time
from myblog.settings import EMAIL_FROM, SECRET_KEY
from users.models import VerifyCodeEmail
from django.utils import timezone

def make_sign():
    """
    生成一个加密字符串
    时间戳+Django秘钥, 通过md5加密
    :return:
    """
    # 时间戳
    times = str(time.time())
    sing_str = times + SECRET_KEY
    md5 = hashlib.md5()
    md5.update(sing_str.encode())
    sign = md5.hexdigest()
    return sign


def send_verify_email(to_email):
    """
    发送验证邮件的链接
    """
    sign = make_sign()
    # 邮件里面的激活地址
    verify_url = '点击链接激活账号 + https://liucy.fun/user_active?sign='+ sign
    # 将邮件和加密数据绑定到一起
    verify_code = VerifyCodeEmail()
    verify_code.email = to_email
    verify_code.code = sign
    verify_code.code_type = 1
    verify_code.save()

    subject = '邮箱验证'
    html_message = '<p>尊敬的用户您好！</p>' \
                   '<p>感谢您使用工商12栋536搭建的网站。</p>' \
                   '<p>您的邮箱为：%s 。请点击此链接激活您的邮箱：</p>' \
                   '<p><a href="%s">%s<a></p>' % (to_email, verify_url, verify_url)

    # 发送邮件
    # send_mail(subject, '', 发送邮件人, [接收邮件的人], '邮件的文本内容')
    send_mail(subject, '', settings.EMAIL_FROM, [to_email], html_message=html_message)
