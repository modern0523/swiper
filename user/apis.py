from django.http import JsonResponse
from lib.sms import send_vcode, check_vcode

from .models import User
from lib.http import render_json
from common import errors

# API接口
# 发送验证码
def submit_vcode(request):
    # 先从前端获取手机号
    phone = request.GET.get('phone')
    # 在这里做验证，是否是手机号
    # 发送验证码
    result = send_vcode(phone)

    return render_json(result)


# 登录
def login(request):
    # 获取前端提交的数据
    phone = request.POST.get('phone')
    vcode = request.POST.get('vcode')

    # 检查用户的验证码是否正确
    if check_vcode(phone, vcode):
        print("登录成功！")
        # 自动注册账号：给User表添加一条记录
        # User.objects.create(phonenum=phone)
        # 获取或者创建，如果没有该数据则创建并返回数据
        user,created = User.objects.get_or_create(nickname=phone, phonenum=phone)
        # print(user, created)

        # 用session保存登录状态
        request.session['uid'] = user.id

        return render_json(user.to_dict())

    else:
        print("验证码输入错误")
        return render_json("验证码错误", errors.VCODE_ERROR)


