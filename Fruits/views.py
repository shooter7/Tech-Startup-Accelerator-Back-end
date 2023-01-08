from django.http import JsonResponse
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Fruits.serializers import FruitSerializer
import os
import sys


@api_view(['GET', 'POST'])
def fruits_list(request):
    fruits = get_data()
    # get all
    if request.method == 'GET':
        return JsonResponse(fruits, safe=False)
    # add new fruit
    if request.method == 'POST':
        serializer = FruitSerializer(data=request.data)
        if serializer.is_valid():
            fruit_dict = {'id': fruits[-1]['id'] + 1, 'name': serializer.data['name'],
                          'description': serializer.data['description']}
            fruits.append(fruit_dict)
            write_data(json.dumps(fruits))
            return Response(fruits[-1], status=201)
        else:
            return Response(serializer.errors, status=400)


@api_view(['GET', 'DELETE'])
def fruit_details(request, id):
    fruits = get_data()
    # get by id
    if request.method == 'GET':
        for item in fruits:
            if item['id'] == id:
                return JsonResponse(item, safe=False)
        return Response(status=404)
    # delete by id
    if request.method == 'DELETE':
        for item in fruits:
            if item['id'] == id:
                fruits.remove(item)
                write_data(json.dumps(fruits))
                return Response(status=200)
        return Response(status=404)


# read data from json file
def get_data():
    file = open(os.path.abspath('Fruits/fruits.json'), "r", encoding="utf8")
    data = json.loads(file.read())
    file.close()
    return data


# write list of fruits after update
def write_data(str_list):
    file = open(os.path.abspath('Fruits/fruits.json'), "w", encoding="utf8")
    file.write(str_list)
    file.close()
