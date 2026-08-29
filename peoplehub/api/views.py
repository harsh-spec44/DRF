from django.shortcuts import render
from .models import Person
from .serializers import PersonModelSerializer
from  rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin,DestroyModelMixin,UpdateModelMixin,ListModelMixin,RetrieveModelMixin
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['GET','PUT','PATCH'])
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

class MultipleObjAPIView(ListCreateAPIView):
   authentication_classes = [TokenAuthentication]
   queryset = Person.objects.all()
   serializer_class = PersonModelSerializer
   permission_classes = [IsAuthenticated]
   def get(self, request, *args, **kwargs):
      print(request.user)
      response = super().get(request, *args, **kwargs)

      return response

class SingleObjAPIView(RetrieveUpdateDestroyAPIView):
   queryset = Person.objects.all()
   serializer_class = PersonModelSerializer
