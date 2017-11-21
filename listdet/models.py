# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from DjangoUeditor.models import UEditorField


from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

from datetime import datetime
# Create your models here.




@python_2_unicode_compatible
class Post(models.Model):
    type = models.CharField(max_length=10, verbose_name=u"类别")
    title = models.CharField(max_length=30, verbose_name=u"标题")
    image = models.ImageField(upload_to="fengmian/%Y/%m", verbose_name=u"封面", max_length=100)
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    author = models.CharField(max_length=10, verbose_name=u"作者")
    detail = UEditorField(verbose_name="文章内容", width=600, height=900,  imagePath="chatu/ueditor/", filePath="chatu/ueditor/", default="")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

class Banner(models.Model):
    type = models.CharField(max_length=10, verbose_name=u"类别")
    title = models.CharField(max_length=30, verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name=u"轮播图", max_length=100)
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    author = models.CharField(max_length=10, verbose_name=u"作者")
    detail = UEditorField(verbose_name="文章内容", width=600, height=900,  imagePath="lunbo/ueditor/", filePath="lunbo/ueditor/", default="")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
