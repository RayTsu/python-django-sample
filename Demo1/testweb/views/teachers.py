from django.shortcuts import render
from django.shortcuts import redirect
from testweb import models

def get_teachers(request):
    cls_list = models.Classes.objects.all()
    return render(request,'get_teachers.html',{'cls_list':cls_list})


def add_teachers(request):
    if request.method == "GET":
        teachers_list = models.Teachers.objects.all()
        return render(request,'add_teachers.html',{'teachers_list':teachers_list})
    elif request.method == "POST":
        nid = request.POST.get('titile')
        teachers_id = request.POST.getlist('teachers_id')
        obj = models.Classes.objects.create(titile=nid)
        obj.m.add(*teachers_id)
        return redirect('/get_teachers.html')

def del_teachers(request):
    nid = request.GET.get('nid')
    models.Classes.objects.filter(id=nid).delete()
    return redirect('/get_teachers.html')

def edit_teachers(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        obj = models.Classes.objects.filter(id=nid).first()
        teachers_list = models.Teachers.objects.all()
        return render(request,'edit_teachers.html',{'nid':nid,'obj':obj,'teachers_list':teachers_list})
    elif request.method == "POST":
        n = request.POST.get('nid')
        t = request.POST.get('titile')
        teachers_id = request.POST.getlist('teachers_id')
        obj = models.Classes.objects.filter(id=n).update(
            id=n,
            titile=t,
        )
        obj.m.add(*teachers_id)
        return redirect('/get_teachers.html')