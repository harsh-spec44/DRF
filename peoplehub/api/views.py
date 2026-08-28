from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer, PersonModelSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from  rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET','POST','PATCH'])
def singleobj(request, id):
    
    data = get_object_or_404(Person,id=id)

    if request.method == "PUT":
        stream = io.BytesIO(request.body)
        parsed_data = JSONParser().parse(stream)
        serilaizer = PersonModelSerializer(data,data=parsed_data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response({'update':'success'})
        return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PATCH":
         stream = io.BytesIO(request.body)
         parsed_data = JSONParser().parse(stream)
         serilaizer = PersonModelSerializer(data,data=parsed_data, partial=True)
         if serilaizer.is_valid():
            serilaizer.save()
            return Response({'update':'success'})
         return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    if request.method == 'GET':

     serilaizer = PersonModelSerializer(data)
     return Response(serilaizer.data)

@api_view(['GET','POST'])
def multiobj(request):

    if request.method == "POST":
        json = request.body
        stream = io.BytesIO(json)
        parsed_data = JSONParser().parse(stream)
        serilaizer = PersonModelSerializer(data = parsed_data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response({"create":"successfull"}, status=status.HTTP_201_CREATED)

        return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
     data = Person.objects.all()
     serilaizer = PersonModelSerializer(data,many=True)
     return Response(serilaizer.data)