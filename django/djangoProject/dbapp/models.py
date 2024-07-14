from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
#from django.core.validators import MinLengthValidator

class User(models.Model):
    userAccount = models.CharField(max_length=150, unique=True)   #用户名，也可以直接是ID
    passwd = models.CharField(max_length=150)    #密码，就不加密了
    username = models.CharField(max_length=150, unique=True)   #这个可有可无，没用就删掉
    register_time = models.DateTimeField()
    is_supperuser=False    #是不是管理员，在后台可以直接改这个属性应该
    class Meta:
        managed = True
        db_table = 'User'



#创建表，应该一对多吧，每一个人对应一个表，表里面是一个人的所有request
class UserRequest(models.Model):
    userAccount = models.CharField(max_length=150, unique=True)
    requestText = models.TextField(verbose_name='请求')
    requestTime = models.DateTimeField(help_text="用户发送请求的时间")
    answerText = models.TextField(verbose_name='回答')    #回答的文本内容
    answerPhoto = models.URLField(max_length=200, verbose_name='Image URL')  #图片和视频的路径,但是需要分开吗？
    answerVideo = models.URLField(max_length=200, verbose_name='video URL')
    answerTime = models.DateTimeField(help_text="用户接到回复的时间")


    class Meta:
        managed = True
        db_table = 'Request'
