from django.shortcuts import render
from .models import blog
from rest_framework.decorators import api_view
from .searliazer import blogSerialziers
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def getalldata(request):
    userdata=blog.objects.all()
    userserial=blogSerialziers(userdata,many=True)
    return Response(userserial.data)

@api_view(['GET'])
def getid(request,id):
    try:
        stid=blog.objects.get(id=id)
    except blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    userserial=blogSerialziers(stid)
    return Response(userserial.data)
    

@api_view(['POST'])
def saveuser(request):
    if request.method=='POST':
        userserial=blogSerialziers(data=request.data)
        if userserial.is_valid():
            userserial.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','DELETE'])
def deleteuser(request,id):
    try:
        stid=blog.objects.get(id=id)
    except blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        userserial=blogSerialziers(stid)
        return Response(userserial.data)
    if request.method=='DELETE':
        blog.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['GET','PUT'])
def updateuser(request,id):
    try:
        stid=blog.objects.get(id=id)
    except blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        userserial=blogSerialziers(stid)
        return Response(userserial.data)
    if request.method=='PUT':
        userserial=blogSerialziers(data=request.data,instance=stid)
        if userserial.is_valid():
            userserial.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    



