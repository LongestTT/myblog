# usrs\urls.py文件
from django.urls import path

from users import views

urlpatterns = [
    path('', views.index),
    path('user_register', views.user_register, name='user_register'),  # 注册
    path('user_login', views.user_login, name='user_login'),  # 登录
    path('user_active', views.user_active, name='user_active'),  # 用户激活
    path('user_logout', views.user_logout, name='user_logout'),  # 用户激活

]
