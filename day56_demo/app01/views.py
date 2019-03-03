from django.shortcuts import render,HttpResponse
from .models import *
import json
# Create your views here.
def get_students(request):
    students_list=Students.objects.all()
    cls_list=Classes.objects.all()
    return render(request,'students.html',{"students_list":students_list,
                                               "cls_list":cls_list,
                                                                                     })

def add_student(request):
    response={'status':True,'message':None,'data':None}
    try:
        username=request.POST.get('username')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        cls_id=request.POST.get('cls_id')
        obj=Students.objects.create(name=username,age=age,gender=gender,cs_id=cls_id)
        response['data']=obj.id
    except Exception as e:
        response['status']=False
        response['message']='输入格式错误!'

    result=json.dumps(response)
    return HttpResponse(result)

def del_student(request):
    response={'status':True}
    try:
        nid=request.GET.get('nid')
        Students.objects.filter(id=nid).delete()
    except Exception as e:
       pass
    result=json.dumps(response)
    return HttpResponse(result)

def edit_student(request):
    response={'code':1000,'message':None}
    print(request.POST)
    try:
        nid=request.POST.get('nid')
        name=request.POST.get('username')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        cs_id=request.POST.get('cls_id')
        Students.objects.filter(id=nid).update(name=name,age=age,gender=gender,cs_id=cs_id)

    except Exception as e:
        response['code']=1001
        response['message']=str(e)
    return HttpResponse(json.dumps(response))

