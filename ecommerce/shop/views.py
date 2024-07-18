from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentData
from .serializer import studentSerializer
from rest_framework.renderers import JSONRenderer
# Create your views here.
def stuinfo(request,pk):
    studentD = StudentData.objects.get(id=pk) # got the complex data
    serializer = studentSerializer(studentD ) # convert to python native
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type ='application/json')

def stuinfolist(request):
    stu = StudentData.objects.all()
    serial = studentSerializer(stu,many=True)
    json_data = JSONRenderer().render(serial.data)
    return HttpResponse(json_data,content_type = 'application/json')