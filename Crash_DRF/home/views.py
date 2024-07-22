from django.shortcuts import render
from rest_framework.decorators import api_view
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
