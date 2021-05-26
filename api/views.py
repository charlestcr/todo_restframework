from api.models import Task
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Taskserializer
from .models import Task

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {

        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'UPdate':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',



    }
    return Response(api_urls)
    
@api_view(['GET'])
def taskList(request):
    tasks=Task.objects.all()
    serializer = Taskserializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request,pk):
    tasks=Task.objects.get(id=pk)
    serializer = Taskserializer(tasks,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
   
    serializer = Taskserializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['POST'])
def taskUpdate(request,pk):
    task=Task.objects.get(id=pk)
    serializer = Taskserializer(instance=task,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()

    return Response("Item succesfully deleted")