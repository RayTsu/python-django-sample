from django.shortcuts import render
from django.shortcuts import redirect
from testweb import models

def get_classes(request):
    cls_list = models.Classes.objects.all()
    return render(request,'get_classes.html',{'cls_list': cls_list})

def add_classes(request):
    if request.method == "GET":
        return render(request,'add_classes.html')
    elif request.method == "POST":
        title = request.POST.get('titile')
        models.Classes.objects.create(titile=title)
        return redirect('/get_classes.html')

def del_classes(request):
    nid = request.GET.get('nid')
    models.Classes.objects.filter(id=nid).delete()
    return redirect('/get_classes.html')

def edit_classes(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = models.Classes.objects.filter(id=nid).first()
        return render(request,'edit_classes.html',{'obj':obj})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        title = request.POST.get('title')
        models.Classes.objects.filter(id=nid).update(titile=title)
        return redirect('/get_classes.html')