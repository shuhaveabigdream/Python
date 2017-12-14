from django.contrib import admin
from .models import file

class fileadmin(admin.ModelAdmin):
    list_display = ("name","createtime")

admin.site.register(file,fileadmin)
