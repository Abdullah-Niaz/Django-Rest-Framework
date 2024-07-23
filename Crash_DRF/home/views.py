from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.response import Response
from .serializer import TodoSerailizer
from .models import Todo
# Create your views here.


@api_view(['GET'])
def home(request):
    return Response({
        "status": 200,
        "message": "Yes Django Rest Framework is Working ! ",
        "method_called": "You called the Get Method"
    })


@api_view(['GET', 'POST', 'PATCH', 'PUT', 'DELETE', 'HEAD'])
def hello_world(request):
    if request.method == 'GET':
        return Response({
            "status": 200,
            "message": "Yes Django Rest Framework is Working ! ",
            "method_called": "You called the GET Method"
        })

    elif request.method == 'POST':
        return Response({
            "status": 200,
            "message": "Yes Django Rest Framework is Working ! ",
            "method_called": "You called the POST Method"
        })
    elif request.method == 'PATCH':
        return Response({
            "status": 200,
            "message": "Yes Django Rest Framework is Working ! ",
            "method_called": "You called the PATCH Method"
        })
    elif request.method == 'PUT':
        return Response({
            "status": 200,
            "message": "Yes Django Rest Framework is Working ! ",
            "method_called": "You called the PUT Method"
        })
    elif request.method == 'DELETE':
        return Response({
            "status": 200,
            "message": "Yes Django Rest Framework is Working ! ",
            "method_called": "You called the DELETE Method"
        })
    elif request.method == 'HEAD':
        return Response({
            "status": 200,
            "message": "Yes Django Rest Framework is Working ! ",
            "method_called": "You called the HEAD Method"
        })
    else:
        return Response({
            "status": 400,
            "message": "Yes Django Rest Framework is Working ! ",
            "method_called": "You called the Invalid Method"
        })


@api_view(['GET'])
def get_todo(request):
    data_obj = Todo.objects.all()
    serializer = TodoSerailizer(data_obj, many=True)


    return Response({
        "status": True,
        "message": "Data Fetched",
        "data": serializer.data
    })


@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSerailizer(data=data)
        if (serializer.is_valid()):
            serializer.save()
            return Response({
                "status": True,
                "message": "Yes Django Rest Framework is Working ! ",
                "data": serializer.data

            })
        return Response({
            "status": False,
            "message": "Something went wrong ! ",
            "error": serializer.errors
        })
    except Exception as e:
        print(e)
    return Response({
        "status": False,
        "message": "soemthing Went Wrong",
    })



@api_view(['PATCH'])
def patch_todo(request):
    data = request.data
    uid = data.get('uid')

    if not uid:
        return Response({
            "status": False,
            "message": "UID is required",
            "data": {}
        }, status=400)
    
    try:
        obj = Todo.objects.get(uid=uid)
    except Todo.DoesNotExist:
        return Response({
            "status": False,
            "message": "Invalid UID",
            "data": {}
        }, status=404)
    
    serializer = TodoSerailizer(obj, data=data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response({
            "status": True,
            "message": "Updated Successfully",
            "data": serializer.data
        })
    
    return Response({
        "status": False,
        "message": "Invalid Data",
        "data": serializer.errors
    }, status=400)


class TodoView(APIView):
    def get(self, request):
        return Response({
            "status": 200,
            "message": "Yes Django Rest Framework is Working!",
            "method_called": "You called the GET Method"
        })

    def post(self, request):
        return Response({
            "status": 200,
            "message": "Yes Django Rest Framework is Working!",
            "method_called": "You called the POST Method"
        })

    def patch(self, request):
        data = request.data
        uid = data.get('uid')

        if not uid:
            return Response({
                "status": False,
                "message": "UID is required",
                "data": {}
            }, status=400)
        
        try:
            obj = Todo.objects.get(uid=uid)
        except Todo.DoesNotExist:
            return Response({
                "status": False,
                "message": "Invalid UID",
                "data": {}
            }, status=404)
        
        serializer = TodoSerailizer(obj, data=data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True,
                "message": "Updated Successfully",
                "data": serializer.data
            })
        
        return Response({
            "status": False,
            "message": "Invalid Data",
            "data": serializer.errors
        }, status=400)

    def delete(self, request):
        return Response({
            "status": 200,
            "message": "Yes Django Rest Framework is Working!",
            "method_called": "You called the DELETE Method"
        })

from rest_framework import mixins, viewsets

class Todo_View(viewsets.ReadOnlyModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerailizer