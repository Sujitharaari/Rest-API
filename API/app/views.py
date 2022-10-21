from django.shortcuts import render
from .models import Drink
from .serializer import DrinkSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer (drinks, many=True)
        return JsonResponse({'drinks':serializer.data}, safe=False)
    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

@api_view(['GET', 'PUT', 'DELETE'])
def detail(request, id):
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return JsonResponse({'error':'Drink not found'}, status=404)
    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        drink.delete()
        return JsonResponse({}, status=204)