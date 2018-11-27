from django.shortcuts import render
from cmdb import models
# Create your views here.
from django.shortcuts import HttpResponse

# user_list = [
#     {"user":"jack","pwd":"abc"},
#     {"user":"tom","pwd":"ABC"},
# ]

def index(request):
    #return HttpResponse("Hello World!")
    #return render(request, "index1.html")
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        print(username,password)
        #添加数据到数据库
        models.UserInfo.objects.create(user=username,pwd=password)
    #从数据库中读取所有数据
    user_list = models.UserInfo.objects.all()
        #temp={"user":username,"pwd":password}
        #user_list.append(temp)
    return render(request,"index.html",{"data":user_list})