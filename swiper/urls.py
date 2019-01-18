"""swiper URL Configuration

"""
from django.conf.urls import url

from user import apis as user_api


urlpatterns = [
    url(r'^api/user/submit/vcode/$', user_api.submit_vcode),
    url(r'^api/user/submit/login/$', user_api.login),

]
