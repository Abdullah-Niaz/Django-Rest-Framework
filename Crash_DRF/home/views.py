from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(['GET'])
def home(request):
    return Response({
        "status":200,
        "message": "Yes Django Rest Framework is Working ! ",
        "method_called":"You called the Get Method"
        })

@api_view(['GET', 'POST','PATCH','PUT','DELETE','HEAD'])
def hello_world(request):
    if request.method == 'GET':
        return Response({
        "status":200,
        "message": "Yes Django Rest Framework is Working ! ",
        "method_called":"You called the GET Method"
        })

    elif request.method == 'POST':
        return Response({
        "status":200,
        "message": "Yes Django Rest Framework is Working ! ",
        "method_called":"You called the POST Method"
        })
    elif request.method == 'PATCH':
        return Response({
        "status":200,
        "message": "Yes Django Rest Framework is Working ! ",
        "method_called":"You called the PATCH Method"
        })
    elif request.method == 'PUT':
        return Response({
        "status":200,
        "message": "Yes Django Rest Framework is Working ! ",
        "method_called":"You called the PUT Method"
        })
    elif request.method == 'DELETE':
        return Response({
        "status":200,
        "message": "Yes Django Rest Framework is Working ! ",
        "method_called":"You called the DELETE Method"
        })
    elif request.method == 'HEAD':
        return Response({
        "status":200,
        "message": "Yes Django Rest Framework is Working ! ",
        "method_called":"You called the HEAD Method"
        })
    else:
        return Response({
        "status":400,
        "message": "Yes Django Rest Framework is Working ! ",
        "method_called":"You called the Invalid Method"
        })

@api_view(['POST'])
def post_todo(request):
    try:
        data  = request.data
        return Response({
            "status":True,
            "message": "Yes Django Rest Framework is Working ! ",
        })
    except Exception as e:
        print(e)
    return Response({
        "status":False,
        "message": "soemthing Went Wrong",
    })