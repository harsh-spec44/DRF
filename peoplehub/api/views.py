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
        parsed_data = request.data
        serilaizer = PersonModelSerializer(data,data=parsed_data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response({'update':'success'})
        return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PATCH":
         parsed_data = request.data
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
        parsed_data = request.data
        serilaizer = PersonModelSerializer(data = parsed_data)
        serilaizer.is_valid(raise_exception=True)
        serilaizer.save()
        return Response({"create":"successfull"}, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
     print(request.accepted_renderer)
     data = Person.objects.all()
     serilaizer = PersonModelSerializer(data,many=True)
     return Response(serilaizer.data)