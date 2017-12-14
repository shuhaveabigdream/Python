from django.db import models

# Create your models here.
class file(models.Model):
    name=models.CharField(u'文件名',max_length=50)
    path=models.CharField(u'文件路径',max_length=50)
    createtime=models.DateTimeField(u'创建时间',auto_now_add=True,editable=False)
    def __str__(self):
        return self.name