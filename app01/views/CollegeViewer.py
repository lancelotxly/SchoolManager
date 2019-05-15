from django.shortcuts import render,redirect,HttpResponse
from app01.models import Depart,Teacher,Student

def college(req):
    Dep_list = Depart.objects.all()
    t_num = Teacher.objects.all().count()
    s_num = Student.objects.all().count()
    context = {
        'Dep_list':Dep_list,
        't_num':t_num,
        's_num':s_num
    }
    return render(req,'college.html',context)

def addCollege(req):
    college_name = req.POST.get('college_name')
    Depart.objects.create(Dname=college_name)
    return HttpResponse('ok')

def delCollege(req):
    college_id = req.POST.get('college_id')
    Depart.objects.filter(id=college_id).delete()
    return HttpResponse('ok')

def setCollege(req):
    college_id = req.POST.get('college_id')
    college_name = req.POST.get('college_name')
    Depart.objects.filter(id=college_id).update(Dname=college_name)
    return HttpResponse('ok')