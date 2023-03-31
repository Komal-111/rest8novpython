
from django.shortcuts import render
from .models import mynotes
from rest_framework.decorators import api_view
from .searliazer import userSerialziers
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def getalldata(request):
    userdata=mynotes.objects.all()
    userserial=userSerialziers(userdata,many=True)
    return Response(userserial.data)

@api_view(['GET'])
def getid(request,id):
    try:
        stid=mynotes.objects.get(id=id)
    except mynotes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    userserial=userSerialziers(stid)
    return Response(userserial.data)
    

@api_view(['POST'])
def saveuser(request):
    if request.method=='POST':
        userserial=userSerialziers(data=request.data)
        if userserial.is_valid():
            userserial.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','DELETE'])
def deleteuser(request,id):
    try:
        stid=mynotes.objects.get(id=id)
    except mynotes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        userserial=userSerialziers(stid)
        return Response(userserial.data)
    if request.method=='DELETE':
      mynotes.delete(stid)
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['GET','PUT'])
def updateuser(request,id):
    try:
        stid=mynotes.objects.get(id=id)
    except mynotes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        userserial=userSerialziers(stid)
        return Response(userserial.data)
    if request.method=='PUT':
        userserial=userSerialziers(data=request.data,instance=stid)
        if userserial.is_valid():
            userserial.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
