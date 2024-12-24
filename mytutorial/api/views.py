from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer


@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postData(request):
    serializer = ItemSerializer(data=request.data)
    if (serializer.is_valid()):
        serializer.save()
    return Response(request.data)


api = "https://api.freeapi.app/api/v1/public/randomusers"


@api_view(["GET"])
def randomusers(request):
    response = requests.get(api)  #
    data = response.json()
    # return Response({
    #     "all_data": data,
    # })
    return render(request, 'randomusers.html', {'data': data})
