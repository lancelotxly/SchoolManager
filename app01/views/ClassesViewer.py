from django.shortcuts import render,redirect,HttpResponse
from app01.models import Depart,Classes

def classes(req):
    Depart_list = Depart.objects.all()
    Cls_list = Classes.objects.all()

    context = {
        'college_list':Depart_list,
        'cls_list':Cls_list
    }
    return render(req,'classes.html',context)

def addClass(req):
    class_name = req.POST.get('class_name')
    college_id = req.POST.get('college_id')
    Dep = Depart.objects.filter(id=college_id).first()
    Classes.objects.create(Clsname=class_name,Dep=Dep)
    return HttpResponse('ok')

def delClass(req):
    cls_id = req.POST.get('cls_id')
    Classes.objects.filter(id=cls_id).delete()
    return HttpResponse('ok')

def setClass(req):
    class_name = req.POST.get('class_name')
    college_id = req.POST.get('college_id')
    cls_id = req.POST.get('cls_id')
    print(class_name,college_id,cls_id)
    Dep = Depart.objects.filter(id=college_id).first()
    Classes.objects.filter(id=cls_id).update(Clsname=class_name,Dep=Dep)
    return HttpResponse('ok')