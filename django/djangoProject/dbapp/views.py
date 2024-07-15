from .models import User,UserRequest
import pandas as pd
from django.http import HttpResponse
#创建一个用户
def creatUser(userAccount , passwd , username):
    User.objects.create(userAccount = userAccount , passwd = passwd , username=username)
#创建管理员
def createSuperUser(userAccount , passwd , username):
    User.objects.create(userAccount=userAccount, passwd=passwd, username=username , is_superuser=True)
#用户改密码
def changePasswd(request,userAccount,newpasswd):
    User.objects.filter(userAccount=userAccount).update(passwd=newpasswd)
#用户改用户名
def changePasswd(request,userAccount,newname):
    User.objects.filter(userAccount=userAccount).update(username=newname)
#把普通用户编变成管理员
def changeToSupperuser(userAccount):
    User.objects.filter(userAccount=userAccount).update(is_superuser=True)
#删除用户（是否需要同时删除请求表中该用户的请求呢？需要的话把注释解掉）
def deleteUser(request,userAccount):
    User.objects.filter(userAccount=userAccount).delete()
    #UserRequest.objects.filter(userAccount=userAccount).delete()

#向数据库中添加用户请求以及回答
def addRequest(request,userAccount,requestText,requestTime,answerTime,requestapi,answerText=None,answerPhoto= None , answerVideo= None ):
    UserRequest.objects.create(userAccount=userAccount,
                               requestText=requestText,
                               requestTime=requestTime,
                               answerTime=answerTime,
                               answerText=answerText,
                               answerPhoto=answerPhoto,
                               answerVideo=answerVideo，
                               requestapi=requestapi)
#删除某一次请求
def deleteRequest(request,userAccount , requestText , requestTime):
    UserRequest.objects.filter(userAccount = userAccount,requestText=requestText,requestTime=requestTime).delete()
#有返回值，一个用户的所有请求,返回一个UserRequest对象的QuerySet,,并被导出到excel
def aUsersRequest_to_excel(request,userAccount):
    Request=UserRequest.objects.filter(userAccount=userAccount).all()
    data = list(Request.values())
    df = pd.DataFrame(data)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=user_requests.xlsx'
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='UserRequests')
    return response
#所有用户的请求，返回一个UserRequest对象的QuerySet,并被导出到excel
def UsersRequest_to_excel(request):
    Request = UserRequest.objects.all()
    data = list(Request.values())
    df = pd.DataFrame(data)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=user_requests.xlsx'
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='UserRequests')
    return response



#这是要放在urls.py里面的，这样子在前端给一个<a>标签就可以下载了
#from django.urls import path
#from . import views

#urlpatterns = [
#    path('export_user_requests/<str:userAccount>/', views.aUsersRequest_to_excel, name='export_user_requests'),
#    path('export_all_requests/', views.UsersRequest_to_excel, name='export_all_requests'),
#]
