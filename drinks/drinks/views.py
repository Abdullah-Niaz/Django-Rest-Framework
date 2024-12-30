from django.http import HttpResponse, response
from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Drink
from rest_framework import viewsets
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework import status


class modelViewDrinkList(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer


# @api_view(['GET', 'POST'])
# def drink_list(request):
#     if request.method == 'GET':
#         drinks = Drink.objects.all()
#         drink_serializer = DrinkSerializer(drinks, many=True)
#         return Response(drink_serializer.data)
#     elif request.method == 'POST':
#         drink_serializer = DrinkSerializer(data=request.data)
#         if drink_serializer.is_valid():
#             drink_serializer.save()
#             return Response(drink_serializer.data)
#         return Response(drink_serializer.errors)
