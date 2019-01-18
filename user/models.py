from django.db import models
import datetime
from lib.orm import ModelMixin

# 用户模型
class User(models.Model, ModelMixin):
    nickname = models.CharField(max_length=32, unique=True)
    phonenum = models.CharField(max_length=16, unique=True)
    sex = models.BooleanField(default=True)  # 性别，默认是True表示男
    avatar = models.CharField(max_length=256)  # 头像地址
    location = models.CharField(max_length=128)  # 位置
    birth_year = models.IntegerField(default=2000)  # 出生年
    birth_month = models.IntegerField(default=1)  # 出生月
    birth_day = models.IntegerField(default=1)  # 出生日

    # 让age函数可以通过点语法调用,如user.age
    @property
    def age(self):
        today = datetime.date.today()
        birth_date = datetime.date(self.birth_year, self.birth_month, self.birth_day)
        ages = (today - birth_date).days // 365
        return ages

    # 重写to_dict
    def to_dict(self):
        return {
            'uid': self.id,
            'nickname': self.nickname,
            'phonenum': self.phonenum,
            'sex': self.sex,
            'avatar': self.avatar,
            'location': self.location,
            'age': self.age
        }
