from django.shortcuts import render
from django.shortcuts import redirect
from testweb import models

def get_students(request):
    stu_list = models.Student.objects.all()
    return render(request,'get_students.html',{'stu_list':stu_list})

def add_students(request):
    if request.method == 'GET':
        cs_list = models.Classes.objects.all()
        return render(request,'add_students.html',{'cs_list':cs_list})
    elif request.method == 'POST':
        u = request.POST.get('username')
        a = request.POST.get('age')
        g = request.POST.get('gender')
        c = request.POST.get('cs')
        models.Student.objects.create(
            username=u,
            age=a,
            gender=g,
            cs_id=c
        )
    return redirect('/get_students.html')

def del_students(request):
    nid = request.GET.get('nid')
    models.Student.objects.filter(id=nid).delete()
    return redirect('/get_students.html')

def edit_students(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        obj = models.Student.objects.filter(id=nid).filter()
        cls_list = models.Classes.objects.all()
        return render(request,'edit_students.html',{'obj':obj,'cls_list':cls_list})
    elif request.method == "POST":
        u = request.POST.get('username')
        a = request.POST.get('age')
        g = request.POST.get('gender')
        c = request.POST.get('cs')
        models.Student.objects.create(
            username=u,
            age=a,
            gender=g,
            cs_id=c
        )
    return redirect('/get_students.html')

