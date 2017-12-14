from django.conf.urls import url
from .views import welcome,Download,Upload,Resorce
urlpatterns = [
    url(r'^Download',Download),#下载资源
    url(r'^Upload',Upload),#上传资源
    url(r'^Resource',Resorce),
    url(r'^',welcome),#主页
]