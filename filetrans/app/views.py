from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.http.response import HttpResponse
from django.http.response import StreamingHttpResponse
from .models import file
import os
def welcome(requests):
    return render(requests,"welcom.html")
def Download(requests):
    if requests.method=="GET":
        filelist=file.objects.all();
        temp="<table><tr>"
        if filelist:
            for item in filelist:
                temp+='<td><a href="Resource/'+item.name+'">'+item.name+"</a></td>"
            temp+="</tr></table>"
            html = render_to_string("downapge.html")
            html=html.replace("{alldate}",temp)
            return HttpResponse(html)
        else:
            return HttpResponse("没有任何文件")
    return HttpResponse("<h1>下载页面</h1>")

path=os.path.dirname(os.path.realpath(__file__))+"/Resorce/"
def Upload(requests):
    if requests.method=="GET":
        return render(requests,"uploadpage.html")
    else:
        date=requests.FILES.get("myfile", None)
        copy = open(path + date.name, 'wb+')
        for item in date:
            copy.write(item)
        copy.close()
        file.objects.create(name=date.name,path=path+date.name)
        return HttpResponse("Upload succeed!")
def Resorce(requests):
    name=requests.path[10:]
    name=path+name
    def file_iterator(file_name, chunk_size=512):
        with open(file_name,'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    response=StreamingHttpResponse(file_iterator(name),content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(name)
    return  response
